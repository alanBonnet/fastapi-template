import os
from typing import TypedDict
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(".") / ".env"

load_dotenv(env_path)


class DbConfig:
    """
    Define los detalles de configuración para la conexión a una base de datos.

    Atributos:
    - `username`: Usuario para la conexión a la base de datos.
    - `password`: Contraseña para la conexión a la base de datos.
    - `dbname`: Nombre de la base de datos.
    - `host`: Dirección del host de la base de datos.
    - `identidad`: Nombre que representa la configuración de la base de datos.
    - `driver_age`: Año de versión del driver de la base de datos (p. ej., 2008, 2012).
    - `port`: Puerto en el que se escucha la base de datos.

    Ejemplos de `driver_age` y drivers:
    - 2018: "ODBC Driver 18 for SQL Server"
    - 2017: "ODBC Driver 17 for SQL Server"
    - 2012: "SQL Server Native Client 11.0"
    - 2008: "SQL Server Native Client 10.0"
    """

    def __init__(
        self,
        username: str,
        password: str,
        dbname: str,
        host: str,
        identidad: str,
        driver_age: int | None = None,
        port: int | None = None,
    ):
        self.username: str = username
        self.password: str = password
        self.dbname: str = dbname
        self.host: str = host
        self.identidad: str = identidad

        driver_sql = {
            # acá podría agregarse a futuro el año de versión y su driver correspondiente para la db
            # https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
            #
            # este es la documentacion para pyobdc para conecciones a dbs
            # https://github.com/mkleehammer/pyodbc/wiki
            # ejemplos con el caso de pyobdc para SQL SERVER
            2018: "?driver=ODBC+Driver+18+for+SQL+Server",
            20173: "?driver=ODBC+Driver+17.3+for+SQL+Server",
            2017: "?driver=ODBC+Driver+17+for+SQL+Server",
            2012: "?driver=SQL+Server+Native+Client+11.0",
            2008: "?driver=SQL+Server+Native+Client+10.0",
        }
        self.driver_age: str = driver_sql.get(int(driver_age), driver_sql[2008])
        self.port: str = f":{port}" if port is not None else ""


# database_configs es un listado de configuraciones para Settings
database_configs: list[DbConfig] = [
    DbConfig(  # DB: NOMBRE DE LA BASE DE DATOS PARA DOCUMENTARLO ACA
        identidad="prueba",  # ejemplo
        username=os.getenv("BASE_DE_DATOS__USERNAME"),
        password=os.getenv("BASE_DE_DATOS__PASSWORD"),
        dbname=os.getenv("BASE_DE_DATOS__DBNAME"),
        host=os.getenv("BASE_DE_DATOS__HOST"),
        driver_age=int(os.getenv("BASE_DE_DATOS__DRIVER")),
    ),
]


class DbConfigDict(TypedDict):
    """Aca van los nombres de cada DbConfig.identidad para que ayude con el autocompletado"""

    prueba: str  # nombre del primer DbConfig como ejemplo


class Settings:
    """
    Una clase que gracias a la lista de `DbConfig` proporciona los links para la conexión a las bases de datos a `SQLAlchemy`

    Configuración del proyecto que proporciona las URLs de conexión a las bases de datos.

    Atributos:
    - `PROJECT_NAME`: Nombre del proyecto.
    - `PROJECT_VERSION`: Versión del proyecto.
    - `SECRET_KEY`: Clave secreta para la seguridad.
    - `ALGORITHM_HASH`: Algoritmo de hash para seguridad.
    - `URL_DBs`: Diccionario con las URLs de conexión a las bases de datos.
    - `Identities`: Lista de identidades de las bases de datos configuradas.

    """

    URL_DBs: DbConfigDict = {
        # TODO: ACA SE CONFIGURA LA CONEXIÓN PARA LA CONEXIÓN DE LA BASE DE DATOS SEGÚN CADA DBCONFIG()
        config.identidad: f"mssql+pyodbc://{config.username}:{config.password}@{config.host}{config.port}/{config.dbname}{config.driver_age}"
        for config in database_configs
    }

    PROJECT_NAME: str = "PROYECTO-FAST-API"
    PROJECT_VERSION: str = "1.0"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM_HASH: str = os.getenv("ALGORITHM_HASH")

    Identities: list[str] = [config.identidad for config in database_configs]

    @staticmethod
    def print_db_configurations():
        """
        Imprime la lista de bases de datos configuradas y sus detalles.
        """
        print("-" * 50)
        print("Bases de datos configuradas".center(50, "-"))
        print("-" * 50)
        for identity in Settings.Identities:
            print(f"Identidad: {identity}".center(50, "-"))
            print(f"URL: {Settings.URL_DBs[identity]}".center(50, "-"))
        print("-" * 50)


Settings.print_db_configurations()

settings = Settings()

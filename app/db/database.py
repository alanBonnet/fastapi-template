from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# conecta a la primera base de datos de la lista settings
LocalEngine = create_engine(settings.URL_DBs["prueba"])
LocalSession = sessionmaker(bind=LocalEngine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db_local():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

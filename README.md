# pasos a seguir para correr fastapi

-  instala el entorno virtual primero
```cmd
python -m venv venv
```
- ejecutamos su script para nuestro terminal
```bash
./env/Scripts/activate.bat
```
- en caso de powershell
```ps 
powershell -ExecutionPolicy ByPass -File .\venv\Scripts\Activate.ps1
```
- se crea requirements.txt
- se carga en su interior
```txt
fastapi
uvicorn
```
- Y se ejecuta el comando siguiente para instalar las dependencias:
```bash
pip install -r requirements.txt
```
# hay dos formas de ejecutar fastapi
 ## desde uvicorn con este código base:
 - main.py
```py
from fastapi import FastAPI 
app = FastAPI()
```
 - terminal
```bash 
uvicorn main:app
```

 ## de forma base eligiendo puerto inclusive:
 - main.py
 ```py 
 from fastapi import FastAPI

import uvicorn

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run("main:app", port=3002)
```
- terminal
```bash
py main.py
```


____
# Estructura del proyecto
```txt
proyecto/
│
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   └── module.py
│   │   └── routers.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── module.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── module.py
│   │
|   ├──schemas/
│   |   ├── __init__.py
│   |   └── module.py
|   |
│   └── utils/
│       ├── __init__.py
│       └── cada_utilidad.py
|
├── scripts/
│   └── generate_module.py
│
├── tests/
│   ├── __init__.py
│   └── test_module.py
│
├── .gitignore
├── .env
├── main.py
└── requirements.txt
```

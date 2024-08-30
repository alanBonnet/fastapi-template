from fastapi import FastAPI, responses
import uvicorn
from app.api.routers import router as api_router

# from app.sql_server.database import engine1, Base

app = FastAPI()


# def create_table():
#     Base.metadata.create_all(bind=engine1)

# create_table()


@app.get("/", include_in_schema=False)
def redirigir_a_docs():
    return responses.RedirectResponse(url="/docs")


app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", port=3002, reload=True)

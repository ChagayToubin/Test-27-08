import os
from project.classes.fetchers.my_mongodb.MongoBD import DALMongo
from project.classes.app_maneger.data_retrieval_maneger.data_retrieval_manager import DataRetrievalManager
from fastapi import FastAPI
from project.classes.app_gateway.fastapi_gateway import FastApiGateway


HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "")


fetcher = DALMongo(HOST, DB, COLLECTION, USER, PASSWORD)
app_manager = DataRetrievalManager(fetcher)
app = FastAPI()
gateway = FastApiGateway(app_manager, app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8004)
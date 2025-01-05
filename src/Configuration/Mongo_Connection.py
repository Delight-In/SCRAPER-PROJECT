import pandas as pd
import os, sys
from database_connect import mongo_operation as MO
from src.constant import *
from src.exception import CustomException
from dotenv import load_dotenv

class MongoIo:
    instance = None

    # Set connection to Mongo DB server
    def __init__(self):

        if MongoIo.instance is None:
            URL = load_dotenv(MONGODB_URL_KEY)
            if URL is None:
                raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
            
            MongoIo.instance = MO(client_url=URL, database_name=MONGO_DATABASE_NAME)
        self.instance = MongoIo.instance

    # Store the Scraped data on MongoDB server
    def store_review(self, Product_Name:str, reviews: pd.DataFrame):
        try:
            collection_name = Product_Name.replace(" ","_")
        except Exception as e:
            raise CustomException(e, sys)
        
    # Retrieve the data drom MongoDB server        
    def get_reviews(self, Product_Name: str):
            try:
                data = self.instance.find(collection_name = Product_Name.replace(" ", "_"))
                return data

            except Exception as e:
                raise CustomException(e, sys)
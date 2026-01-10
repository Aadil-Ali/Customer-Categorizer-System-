import pandas as pd
from database_connect import mongo_operation as mongo
import os, sys
from src.constants import *
from src.exception import CustomException

class MongoIO:
    mongo_ins = None

    def __init__(self):
        if MongoIO.mongo_ins is None:
            
            # --- YAHAN CHANGE KIYA HAI ---
            # Direct Cloud URL (Tere naye password ke sath)
            mongo_db_url = "mongodb+srv://aadilansari123456_db_user:aadil123@cluster0.b9o3ptc.mongodb.net/?retryWrites=true&w=majority"
            
            # Humne wo 'Environment Key' wali line HATA DI hai.
            # Ab code seedha connect karega.
            
            MongoIO.mongo_ins = mongo(client_url=mongo_db_url,
                                    database_name=MONGO_DATABASE_NAME)
        self.mongo_ins = MongoIO.mongo_ins

    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        try:
            collection_name = product_name.replace(" ", "_")
            self.mongo_ins.bulk_insert(reviews,
                                     collection_name)

        except Exception as e:
            raise CustomException(e, sys)

    def get_reviews(self, product_name: str):
        try:
            data = self.mongo_ins.find(
                collection_name=product_name.replace(" ", "_")
            )

            return data

        except Exception as e:
            raise CustomException(e, sys)
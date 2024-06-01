import os
import sys
from src.exception import CustomException
from src.logging import logging
from dataclasses import dataclass
from src.utils import read_sql_data

@dataclass
class DataIngestionConfig:
    train_data_path:str= os.path.join('artifact', 'train.csv')
    test_date_path:str= os.path.join('artifact', 'test.csv')
    raw_data_path:str= os.path.join('artifact', 'raw.csv')



class dataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Reading from mysql")
            df=read_sql_data()
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
        except Exception as e:
            raise CustomException(e, sys)

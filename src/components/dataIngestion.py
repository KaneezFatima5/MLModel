import os
import sys
from src.exception import CustomException
from src.logging import logging
from dataclasses import dataclass
from src.utils import read_sql_data
from sklearn.model_selection import train_test_split

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

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set=train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_date_path, index=False, header=True)

            return(self.ingestion_config.train_data_path, self.ingestion_config.test_date_path)

        except Exception as e:
            raise CustomException(e, sys)

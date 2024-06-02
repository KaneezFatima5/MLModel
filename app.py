from src.logging import logging
from src.exception import CustomException
from src.components.dataIngestion import dataIngestion
import sys

if __name__ == "__main__":
    logging.info("execution started")
    try:
        dataIngestion=dataIngestion()
        dataIngestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e, sys)
from src.logging import logging
from src.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("execution started")
    try:
        a=1/0
    except Exception as e:
        raise CustomException(e, sys)
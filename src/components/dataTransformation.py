import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

from src.exception import CustomException
from src.logging import logging

@dataclass
def dataTransformtionConfig():
    processor_file_path=os.path.join('artifact', 'preprocessor.pkl')

class datatransformation:
    def __init__(self):
        self.dataTransformationConfig=dataTransformtionConfig()
    
    def get_data_transformer_object(self):
        try:
            # df=pd.read_csv('..notebook/data/raw.scv')
            # numerical_features=[col for col in df.columns if df[col].dtype != 'O']
            # categorical_features=[col for col in df.columns if df[col].dtype == 'O']
            numerical_features=["reading_score", "writing_score"]
            categorical_features=["gender", "race_ethinicity", "parental_level_of_education", "lunch", "test_preparation_course"]
            logging.info(f"there are {len(numerical_features)} numerical features: {numerical_features}")
            logging.info(f"there are {len(categorical_features)} categorical features: {categorical_features}")
            preprocessor= ColumnTransformer(
                [
                    ("oneHotEncoder", OneHotEncoder, categorical_features),
                    ("standardScaler", StandardScaler, numerical_features)
                ]
            )
            return preprocessor
        
        except Exception as e:
            CustomException(e, sys)

    # def intitiate_data_transformation(self, train_path, test_path):

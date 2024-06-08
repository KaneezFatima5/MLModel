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
    
    try:
        df=pd.read_csv('artifact/raw.scv')
        numerical_features=[col for col in df.columns if df[col].dtype != 'O']
        categorical_features=[col for col in df.columns if df[col].dtype == 'O']
    except Exception as e:
        CustomException(e, sys)
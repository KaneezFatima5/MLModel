import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logging import logging


@dataclass
def dataTransformtionConfig():
    processor_file_path=os.path.join('artifact', 'preprocessor.pkl')

class datatransformation:
    def __init__(self):
        self.dataTransformationConfig=dataTransformtionConfig()
    
    try:
        pass
    except Exception as e:
        CustomException(e, sys)
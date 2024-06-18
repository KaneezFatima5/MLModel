import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

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

            numerical_pipeline=Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='median')),
                ("Scaler", StandardScaler())
            ])
            categorical_pipeline=Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='most_frequent')),
                ("OneHotEncoder", OneHotEncoder()),
                ('Scaler', StandardScaler(with_mean=False))
            ])

            preprocessor= ColumnTransformer(
                [
                    ("numPipeline", numerical_pipeline, numerical_features),
                    ("catPipeline", categorical_pipeline, categorical_features)
                ]
            )
            return preprocessor
        
        except Exception as e:
            CustomException(e, sys)

    def intitiate_data_transformation(self, train_path, test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_df)

            logging.info("Reading train and test files")

            pre_processing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns=["writing_score", "reading_score"]

            input_features_train_df=train_df.drop(columns=[target_column_name], axis=1)
            target_features_train_df=train_df[target_column_name]


            input_features_test_df=test_df.drop(columns=[target_column_name], axis=1)
            target_features_test_df=test_df[target_column_name]

            logging.info("Applying preprocessing into train and test dataframe")

            input_feature_train_arr=pre_processing_obj.fit_transform(input_features_train_df)
            input_features_test_arr=pre_processing_obj.fit(input_features_test_df)

            train_arr=np.c_[
                input_feature_train_arr, np.array(target_features_train_df)
            ]
            test_arr= np.c_[
                input_features_test_arr, np.array(target_features_test_df)
            ]

            save_object(
                file_path=self.dataTransformationConfig.processor_file_path,
                obj=pre_processing_obj
            )

            return(
                train_arr,
                test_arr,
                self.dataTransformationConfig.processor_file_path
            )


        except Exception as e:
            raise CustomException(e, sys)
        

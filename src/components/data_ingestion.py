import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
### dataclass use to create class variables

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    # This will be the path which we are giving to the data ingestion component.
    # And Data Ingestion component output will save all files in this path.
    # Besically all the outputs will be stored in the artifact folder.
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    # These are the inputs I am giving to DataIngestion Component,
    # Now the DataIngestion Component knows where to save the train path, test path, data path.

'''
Decorator dataclass
Inside a class to define a class variable you besically use init right?
But if you try to use this dataclass you will be able to directly define your
class variable.


Why are we creating this class?
Because in data ingestion component any input that is required
I probaly give from this DataIngestionConfig.
'''

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        # What this method will do?
        # If you data is stored in some databases I will write my code over here to read from the database.
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data, test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data, test_data)
    
    modeltrainer=ModelTrainer()
    print(modeltrainer.initate_model_trainer(train_arr,test_arr))

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split



@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')



class DataIngestion:
    def __init__(self):
        self.ingestion_Config=DataIngestionConfig()

    def intiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion class or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info("Exported or Read the data as DataFrame")
            os.makedirs(os.path.dirname(self.ingestion_Config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_Config.raw_data_path,index=False,header=True)
            logging.info("Traintest plate Intiatated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_Config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_Config.test_data_path,index=False,header=True)
            logging.info("ingestion of data completed")
            return(
                self.ingestion_Config.train_data_path,
                self.ingestion_Config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__=="__main__":
    obj=DataIngestion()
    obj.intiate_data_ingestion()


from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeLine:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
        data_ingestion_training_pipeline = DataIngestionTrainingPipeLine()
        data_ingestion_training_pipeline.main() 
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<<")
    except Exception as e:
        raise e      
        
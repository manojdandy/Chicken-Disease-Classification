from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeLine
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeLine
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeLine
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = 'Data Ingestion Stage'

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
        data_ingestion_training_pipeline = DataIngestionTrainingPipeLine()
        data_ingestion_training_pipeline.main() 
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<<")
    except Exception as e:
        raise e   



STAGE_NAME = 'PrePare Base Model Stage'

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
        obj = PrepareBaseModelTrainingPipeLine()
        obj.main() 
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<<")
    except Exception as e:
        raise e 
    

STAGE_NAME = 'Training'

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>> Stage {STAGE_NAME} Started >>>>>>>>>>>')
        obj = ModelTrainingPipeLine()
        obj.main()
        logger.info(f'>>>>>>>> Stage {STAGE_NAME} Completed >>>>>>>>>>>')
    except Exception as e:
        raise e     


STAGE_NAME = 'Evaluation Stage'

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>> Stage {STAGE_NAME} Started >>>>>>>>>>>')
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>>>> Stage {STAGE_NAME} Completed >>>>>>>>>>>')
    except Exception as e:
        raise e     
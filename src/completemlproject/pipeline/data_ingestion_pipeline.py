from src.completemlproject.config.configuration import ConfigurationManager
from src.completemlproject.components.data_ingestion import DataIngestion
from src.completemlproject.logging import logger


STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
         config=ConfigurationManager()
         data_ingestion_config = config.get_data_ingestion_config()
         data_ingestion=DataIngestion(config=data_ingestion_config)
         data_ingestion.download()
         data_ingestion.extract_zip_file()


if __name__=="main":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==============x")
    except Exception as e:
        logger.exception(e)
        raise e


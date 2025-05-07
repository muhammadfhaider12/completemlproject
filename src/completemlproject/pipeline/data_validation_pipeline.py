from src.completemlproject.config.configuration import ConfigurationManager
from src.completemlproject.components.data_validation import DataValiadtion
from src.completemlproject.logging import logger


STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
         config=ConfigurationManager()
         data_validation_config = config.get_data_validation_config()
         data_validation=DataValiadtion(config=data_validation_config)
         data_validation.validate_all_columns()


if __name__=="main":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj= DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==============x")
    except Exception as e:
        logger.exception(e)
        raise e





from src.completemlproject.logging import logger
from src.completemlproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.completemlproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.completemlproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.completemlproject.pipeline.model_trainer_pipeline import ModelTrainerPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation= DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==============x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME="Model Trainer Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer= ModelTrainerPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==============x")
except Exception as e:
    logger.exception(e)
    raise e
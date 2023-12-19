from mlops_project import logger
from mlops_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlops_project.pipeline.stage_02_data_validation import DataValidationPipeline
from mlops_project.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlops_project.pipeline.stage_04_model_training import ModelTrainerPipeline
from mlops_project.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    pipelilne = DataValidationPipeline()
    pipelilne.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    pipelilne = DataTransformationPipeline()
    pipelilne.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    pipelilne = ModelTrainerPipeline()
    pipelilne.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    pipelilne = ModelEvaluationPipeline()
    pipelilne.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
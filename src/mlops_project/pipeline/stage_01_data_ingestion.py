

from mlops_project.components.data_ingestion import DataIngestion
from mlops_project.config.configuration import ConfigurationManager
from mlops_project import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main___":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        pipelilne = DataIngestionTrainingPipeline()
        pipelilne.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
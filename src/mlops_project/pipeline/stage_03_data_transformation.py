from mlops_project import logger

from mlops_project.components.data_transformation import DataTransformation
from mlops_project.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = ConfigurationManager()
        with open(config.get_data_validation_config().STATUS_FILE) as f:
            status = f.read().split()[-1]

        if status == "True":
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
        else:
            raise Exception('Invalid data schema')
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        pipelilne = DataTransformationPipeline()
        pipelilne.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
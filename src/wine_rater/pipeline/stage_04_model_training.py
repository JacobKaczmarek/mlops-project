from wine_rater import logger
from wine_rater.components.model_trainer import ModelTrainer
from wine_rater.config.configuration import ConfigurationManager

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()

        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        pipelilne = ModelTrainerPipeline()
        pipelilne.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} complete <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
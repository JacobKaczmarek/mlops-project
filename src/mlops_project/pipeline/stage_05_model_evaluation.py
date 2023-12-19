from mlops_project.components.model_evaluation import ModelEvaluation
from mlops_project.config.configuration import ConfigurationManager
from mlops_project.entity.config_entity import ModelEvaluationConfig
from mlops_project import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        model_evaluation_config = config_manager.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_to_mlflow()


if __name__ == "__main__":
    try:
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e
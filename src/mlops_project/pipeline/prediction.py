from pathlib import Path
import joblib
from mlops_project.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self):
        config = ConfigurationManager().get_model_evaluation_config()
        self.model = joblib.load(Path(config.model_path))


    def predict(self, input_data):
        return self.model.predict(input_data)

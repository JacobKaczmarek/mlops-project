from urllib.parse import urlparse
from pathlib import Path
import joblib
import mlflow
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from mlops_project.entity.config_entity import ModelEvaluationConfig
from mlops_project.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return { "rmse": rmse, "mae": mae, "r2": r2 }
    
    def log_to_mlflow(self):
        model = joblib.load(self.config.model_path)
        test_data = pd.read_csv(self.config.test_data_path)

        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri = self.config.mlflow_uri
        tracking_url_type_store = urlparse(mlflow.get_registry_uri()).scheme

        with mlflow.start_run():
            predicted = model.predict(test_x)

            scores = self.evaluate(test_y, predicted)
            save_json(path=Path(self.config.metrics_path), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metrics(scores)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNet")
            else:
                mlflow.sklearn.log_model(model, "model")
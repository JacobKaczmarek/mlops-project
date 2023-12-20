import os
import zipfile
import urllib.request as request
from pathlib import Path
from wine_rater import logger
from wine_rater.entity.config_entity import DataIngestionConfig
from wine_rater.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists with size {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
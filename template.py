import os
import logging
from argparse import ArgumentParser
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

parser = ArgumentParser(
    prog='Template',
    description='Script for creating the file tree for a data science project'
)

parser.add_argument('-p', '--project', type=str)
args = parser.parse_args()

project_name = args.project

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    directory, filename = os.path.split(filepath)

    if directory != "" and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Creating directory; {directory} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
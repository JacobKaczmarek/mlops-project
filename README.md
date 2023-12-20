# Wine Rater

## Instalation

To run this project with mlflow in Dagshub you need to create a .env file in the root of the file structure and it has to define the environment variable like this

``` bash
MLFLOW_TRACKING_URI={Your_tracking_URL}
```

Next to run it inside of a Docker containner the following command has to be ran

``` bash
docker build -t wine-rater .
docker run -p 8080:8080 wine-rater
```

After the container was created the web interface will be available under <http://localhost:8080>

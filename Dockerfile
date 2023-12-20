FROM python:3.8-slim-buster

RUN apt -y update

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN python main.py

CMD ["python", "app.py"]

FROM python:3.8-slim-buster

RUN apt upodate -y && apt install awscli -y

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN python main.py

CMD ["python", "app.py"]

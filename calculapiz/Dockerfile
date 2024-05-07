FROM python:3.9

WORKDIR /app

COPY . /app

RUN ["pip3", "install", "-r", "requirements.txt"]

ENV FLASK_APP=calculapiz_app.py

CMD ["flask", "run", "--host", "0.0.0.0"]

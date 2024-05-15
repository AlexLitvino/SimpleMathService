FROM python:3.9

WORKDIR /calculapiz

COPY . /calculapiz

RUN ["pip3", "install", "."]

ENV FLASK_APP=calculapiz_app.py

CMD ["flask", "run", "--host", "0.0.0.0"]



FROM python:3.9-slim-bullseye

ENV FLASK_APP game.app:app

WORKDIR /opt

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY game game

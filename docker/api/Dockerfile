FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./dev-requirements.txt .

COPY ./src/api .

RUN pip install --no-cache-dir --upgrade -r dev-requirements.txt

FROM python:3.12.2-slim

RUN mkdir app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pwd
RUN ls -la

COPY . /app/

RUN python -m venv /py && \
    pip install --upgrade pip && \
    pip install -r requirements/base.txt

# Gunicorn as app server
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 trastero.wsgi:application

EXPOSE 8080
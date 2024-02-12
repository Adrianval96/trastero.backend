FROM python:3.12.2-slim

COPY . /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /py && \
    pip install --upgrade pip && \
    pip install -r requirements/base.txt

# Gunicorn as app server
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 app.wsgi:application

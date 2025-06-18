FROM python:3.11.9

ARG SECRET_KEY
ARG DEBUG

ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=${SECRET_KEY}
ENV DEBUG=${DEBUG}

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app


WORKDIR /app/app
RUN python manage.py collectstatic --noinput

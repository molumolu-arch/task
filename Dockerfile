FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /app/app/
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

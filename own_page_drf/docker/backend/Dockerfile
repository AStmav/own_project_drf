FROM python:3.10

WORKDIR /django_code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -qy upgrade

COPY requirements.txt /django_code/
RUN pip install -r requirements.txt

COPY . /django_code/
EXPOSE 8000
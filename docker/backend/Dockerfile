FROM python:3.10

WORKDIR /django_code



RUN apt update && apt -qy upgrade

COPY requirements.txt /django_code/
RUN pip install -r requirements.txt

COPY . /django_code/
EXPOSE 8000
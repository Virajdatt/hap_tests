FROM python:3.6-slim

RUN apt-get update
RUN apt-get -y install gcc

WORKDIR /app

ADD . /app 



RUN pip install flask textblob

EXPOSE 5000


CMD ["python", "New.py"]
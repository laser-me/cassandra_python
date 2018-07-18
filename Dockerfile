FROM python:3

WORKDIR /usr/src/app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
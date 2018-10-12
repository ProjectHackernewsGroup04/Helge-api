FROM python:3.6
ADD . /helge-api
WORKDIR /helge-api
RUN pip install -r requirements.txt
EXPOSE 5001
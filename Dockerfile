FROM python:3.6
ADD . /helge-api
WORKDIR /helge-api
RUN pip install -r requirements.txt
CMD python3 app/api.py
EXPOSE 5001
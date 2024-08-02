
FROM python:3.12-slim

RUN pip install gunicorn

RUN pip install gevent

ADD requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /src

COPY . .

CMD gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:9008 --access-logfile - --error-logfile - app:app
# Specify the command to run your application

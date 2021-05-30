FROM python:3.8
WORKDIR /app
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev
RUN pip install -U pip
RUN pip install flask
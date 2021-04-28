FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y \
python3-pip \
python3-setuptools \
libsystemd-dev \
# Required for Postgres
libpq-dev \
python3-dev

WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000

ENTRYPOINT python3 app.py runserver > web-application.log
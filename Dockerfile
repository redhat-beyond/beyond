FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y \
python3-pip \
python3-setuptools \
# Required packages for mariadb
libsystemd-dev \
curl \
apt-transport-https \
&& curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup|bash \
&& apt update -y \
&& apt install libmariadb3 libmariadb-dev -y

WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000

ENTRYPOINT python3 app.py runserver > web-application.log

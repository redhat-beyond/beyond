FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Install mysql and run
RUN apt-get install -y python3-setuptools mysql-server mysql-client \
  && usermod -d /var/lib/mysql/ mysql && /etc/init.d/mysql start

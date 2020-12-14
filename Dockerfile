FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-setuptools libsystemd-dev

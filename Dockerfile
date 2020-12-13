FROM ubuntu:18.04
MAINTAINER Canonical

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-setuptools mysql-server mysql-client libsystemd-dev


#!/bin/bash

apt-get update -y
apt-get install python3-pip -y
pip3 install Flask
nohup python3 /vagrant/app.py runserver & sleep 1

#!/bin/bash

apt-get update -y
apt-get install python3-pip -y
pip3 install Flask
cd /vagrant; nohup python3 app.py &

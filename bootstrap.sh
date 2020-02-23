#!/bin/bash

apt-get update -y
apt-get install python3-pip -y
pip3 install flake8
flake8  # execute flake8 on current dir recursively

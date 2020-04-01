#!/bin/bash -x

apt-get update -y
apt-get install python3-pip -y

#if [ $TRAVIS ]
#then
#   my_path=$TRAVIS_BUILD_DIR
#else
#   my_path='/vagrant'
#fi

pwd
pip3 install -r /vagrant/requirements.txt
nohup python3 /vagrant/app.py runserver & sleep 1

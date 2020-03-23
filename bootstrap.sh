#!/bin/bash

apt-get update -y
apt-get install python3-pip -y

if [ $TRAVIS ]
then
   my_path=$TRAVIS_BUILD_DIR
else
   my_path='/vagrant'
fi

pip3 install -r $my_path/requirements.txt
nohup python3 $my_path/app.py runserver & sleep 1

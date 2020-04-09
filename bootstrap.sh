#!/bin/bash -x

apt-get update -y

# Setting MySQL root user password root/root
debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
# Installing packages
apt-get install -y python3-pip mysql-server mysql-client
# create database
mysql -u root -proot  <<MYSQL_SCRIPT
CREATE DATABASE baboon;
USE baboon;
create table users(username VARCHAR(25) NOT NULL, password VARCHAR(100) NOT NULL, creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY(username));
MYSQL_SCRIPT

#if [ $TRAVIS ]
#then
#   my_path=$TRAVIS_BUILD_DIR
#else
#   my_path='/vagrant'
#fi

pip3 install -r requirements.txt
nohup python3 app.py runserver & sleep 1

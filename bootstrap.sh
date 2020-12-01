#!/bin/bash -x

apt-get update -y

# Setting MySQL root user password root/root
debconf-set-selections <<<'mysql-server mysql-server/root_password password root'
debconf-set-selections <<<'mysql-server mysql-server/root_password_again password root'
# Installing packages
apt-get install -y python3-pip python3-setuptools mysql-server mysql-client libsystemd-dev
# create database
systemctl start mysql
mysql -u root -proot <<MYSQL_SCRIPT
CREATE DATABASE beyond;
USE beyond;
create table users(username VARCHAR(25) NOT NULL, password VARCHAR(100) NOT NULL, creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY(username));
MYSQL_SCRIPT

if [ $HOME = "/home/runner" ]; then
  my_path="."
else
  my_path="/vagrant"
fi

pip3 install -r $my_path/requirements.txt
nohup python3 $my_path/app.py runserver &
sleep 1

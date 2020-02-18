#!/bin/bash

apt-get update -y
apt-get install python3-pip -y
yes | pip3 install virtualenv
yes | pip3 install virtualenvwrapper

# make directory for virtual envs. dont fail if it already exists + change permissions to vagrant user
mkdir -p /home/vagrant/.virtualenvs
chown -R vagrant:vagrant /home/vagrant/.virtualenvs

# set WORKON_HOME to our virtualenv dir
echo "export WORKON_HOME=/home/vagrant/.virtualenvs" >> /home/vagrant/.bashrc

# add this to .bashrc so that the virtualenvwrapper commands are loaded.
echo "VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'" >> /home/vagrant/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc

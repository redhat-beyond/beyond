#!/bin/bash

apt-get update -y
apt-get install python3-pip -y
pip3 install --yes virtualenv
pip3 install --yes virtualenvwrapper

# make directory for virtual envs
mkdir ~/.virtualenvs

# set WORKON_HOME to our virtualenv dir
export WORKON_HOME=~/.virtualenvs

# add this to .bashrc so that the virtualenvwrapper commands are loaded.
. /usr/local/bin/virtualenvwrapper.sh

# reload .bashrc and we are ready to go!
. .bashrc


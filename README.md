# baboon

In this repository we learn the functions of git and GitHub


Requirements
-----------------------------
- Install vagrant 'aws' plugin: `vagrant plugin install vagrant-aws`
- Install vagrant 'env' plugin: `vagrant plugin install vagrant-env`
- Copy the .env_template file content to a .env file and insert the required keys.

Some Useful git Commands 
--------------------
git remote -v
      Show all the tracked repositories

git remote add upstream git@github.com:Code-Collaborate-Community/baboon.git
      Adding upstream repo code

git commit -a
      Record changes to the repository

git clone
      Clone a repository into a new directory

git push  
      Update remote refs along with associated objects

Some Userful Vagrant Commands
-----------------------------

vagrant init fedora/31-cloud-base
	Create Vagrant file for Fedora 31 

vagrant up --provider=virtualbox
	Build and run the VM base on the Vagrant file data using VirtualBox
	
How to install virtualenvwrapper on host
---------------------------------------
Install pip3 if not already installed. For Debian based systems such as Debian, Ubuntu Or Linux mint, run the following
command from a terminal:\
`sudo apt install python3-pip`

For Fedora based systems such as Fedora, Cent OS or RHEL, use:\
`sudo dnf install python3-pip`

Once you have pip3 installed, use it to install virtualenvwrapper. Run the following command from a terminal:\
`sudo pip3 install virtualenvwrapper`

After installation, you need to do some configurations to make virtualenvwrapper work. First, you will have to create a
directory to save all virtual environments. Usually, it is the .virtualenvs directory in your home directory:\
`mkdir ~/.virtualenvs`

Now you have to set this as the home directory for your workon command:\
`export WORKON_HOME=~/.virtualenvs`

Next, you have to add some configurations to your .bashrc file. For Debian do:\
`echo VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3' >> ~/.bashrc`\
`echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.bashrc`

For Fedora based systems:\
`echo VIRTUALENVWRAPPER_PYTHON='/usr/local/bin/python3' >> ~/.bashrc`\
`echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.bashrc`

Now, source the updated .bashrc file:\
`source ~/.bashrc`

##### Once Your virtualenvwrapper is installed:
To create a new virtual environment, run:\
`mkvirtualenv name-of-your-virtual-env`

This will create a new virtual environment and activate it for you. To deactivate the virtual environment, run:\
`deactivate`

To activate your virtual environment again, simply run:\
`workon name-of-your-virtual-env`

How to use the database
---------------------------------------
In order to add new tables to the db, insert the respected SQL commands inside the 'MYSQL SCRIPT' clause in the boostrap script.

In order look at the db, run the machine and use the following commands:
open mysql with the password root:\
`mysql -uroot -p`

Use our database:\
`USE baboon;`

See which tables exist in the db:\
`SHOW TABLES;`

See the table structure:\
`DESCRIBE table-name;`

See all the values in the table:\
`SELECT * FROM table-name;`                  

How to use isort
---------------------------------------
isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.

Install isort package:\
`pip install isort` 

Create your python file include imports:\
`vim example.py`

Run isort:\
`isort example.py`

Done! The imports inside your python file is sorted.
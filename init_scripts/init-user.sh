#!/bin/sh
# init-user.sh - Initialize user-level requirements for our project
# Should be set in the Vagrantfilee to run once with low privileges (non-root).

# Add aliases to the vagrant user's .bashrc & execute permission
echo ". /vagrant/aliases.sh" >> ~/.bashrc
chmod +x /vagrant/aliases.sh

# Using pipenv as our default python package manager
# Also, we specify the version to avoid possible inconsistency
# with future releases, and --user to reduce global fingerprint
# on the system as a whole.
python3 -m pip install -I pipenv==2020.8.13 --user
cd /vagrant/sellotape && pipenv sync

# Create required models
pipenv run python3 sellotape_dj/manage.py migrate
# Create default super user
export DJANGO_SUPERUSER_PASSWORD='123456'
pipenv run python3 sellotape_dj/manage.py createsuperuser --noinput --username admin --email admin@localhost
# Load aliases & Start sellotape django webserver
. /vagrant/aliases.sh
start_sellotape &
echo "-----2ND INIT DONE-----"
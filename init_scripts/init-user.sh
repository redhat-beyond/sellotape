#!/bin/sh
# init-user.sh - Initialize user-level requirements for our project
# Should be set in the Vagrantfilee to run once with low privileges (non-root).

# Add aliases to the vagrant user
echo ". ~/.aliases.sh" >> ~/.bashrc
chmod +x ~/.aliases.sh

# Using pipenv as our default python package manager
# Also, we specify the version to avoid possible inconsistency
# with future releases, and --user to reduce global fingerprint
# on the system as a whole.
python -m pip install -I pipenv==2020.8.13 --user
cd /vagrant/sellotape && pipenv sync

# Start sellotape django webserver
pipenv run python sellotape_dj/manage.py runserver 0.0.0.0:8000&
echo "-----2ND INIT DONE-----"
echo "Sellotape running on http://localhost:8000"
#!/bin/sh
# init-user.sh - Initialize user-level requirements for our project
# Should be set in the Vagrantfilee to run once with low privileges (non-root).

# Using pipenv as our default python package manager
# Also, we specify the version to avoid possible inconsistency
# with future releases, and --user to reduce global fingerprint
# on the system as a whole.
python -m pip install -I pipenv==2020.8.13 --user
cd /vagrant/sellotape && python -m pipenv sync
echo "-----2ND INIT DONE-----"

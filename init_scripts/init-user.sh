#!/bin/sh
# Install pipenv and then use it to install a snapshot of
# the packages needed for the project
python -m pip install -I pipenv==2020.8.13 --user
cd /vagrant/sellotape && python -m pipenv sync
echo "-----2ND INIT DONE-----"

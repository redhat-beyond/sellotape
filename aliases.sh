#!/bin/sh
alias start_sellotape="cd /vagrant/sellotape && echo 'Sellotape running on http://localhost:8000'; pipenv run python3 sellotape_dj/manage.py runserver 0.0.0.0:8000"
alias stop_sellotape='kill $(lsof -t -i:8000) 2&>/dev/null'
alias restart_sellotape="stop_sellotape; start_sellotape"
#!/bin/bash

DIR="venv"

[ ! -d "$DIR" ] && python3 -m venv $DIR && source $DIR/bin/activate && pip install wheel && pip install -r requirements.txt

[ -d "$DIR" ] && source $DIR/bin/activate && python manage.py migrate && python manage.py runserver

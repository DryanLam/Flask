#!/bin/bash

export FLASK_ENV=development
export FLASK_APP=main.py

# flask run -p 3500 --reload --debugger
nohup flask run -p 3500 --reload --debugger >> api.out &

#!/bin/bash

export FLASK_ENV=development
export FLASK_APP=main.py

# flask run -p 3000 --reload --debugger
nohup flask run -p 3000 --reload --debugger >> web.out &
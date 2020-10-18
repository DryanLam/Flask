#!/bin/bash

# Install libs
pip3 install -r requirements.txt

# Run with nohup
nohup sh runner.sh > api-server.log &


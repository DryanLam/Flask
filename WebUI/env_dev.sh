#!/bin/bash

# Install libs
sudo pip3 install -r requirements.txt

# Run with nohup
sudo nohup sh runner.sh > webui-server.log &
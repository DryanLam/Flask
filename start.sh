#!/bin/bash

chmod 777 -R ./Docker/redis_dump
ls -la ./Docker/redis_dump

# Deploy database services: Redis - Mongodb - MySQL
docker-compose -f ./Docker/docker-compose.yml up -d

# Initialize base data
# sh ./Docker/restore.sh


# Using docker cli
# docker build -t api .
# docker run --name capi -d -p 3500:3500 --network="host" api


# docker build -t web .
# docker run --name cweb -d -p 3000:3000 --network="host" web


# using for shell
# FOR API
# echo "Starting deploy API server"
# pip3 install -r ./API/requirements.txt

# cd API
# sh runner.sh
# echo "Deployed API service successfully"

# # Return main source
# cd ..

# # FOR WebUI
# echo "Starting deploy Web server"
# pip3 install -r ./WebUI/requirements.txt

# cd WebUI
# sh runner.sh
# echo "Deployed WebUI service successfully"
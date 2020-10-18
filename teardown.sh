#!/bin/bash

echo "Starting tear down process"

sudo kill -9 $(lsof -n -i :3000 | grep LISTEN | awk '{print $2}')
sudo kill -9 $(lsof -n -i :3500 | grep LISTEN | awk '{print $2}')

docker-compose -f ./Docker/docker-compose.yml down

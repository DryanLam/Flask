#!/bin/bash

chmod 777 -R Docker/redisdump
docker-compose -f Docker/docker-compose.yml up -d

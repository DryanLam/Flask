#!/bin/bash

chmod 777 -R Docker/redis_dump

docker-compose -f Docker/docker-compose.yml up -d

sh API/env_dev.sh
sh API/runner.sh
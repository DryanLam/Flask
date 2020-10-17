#!/bin/bash

chmod 777 -R Docker/redis_dump

docker-compose -f Docker/docker-compose.yml up -d

sh Docker/restore.sh

sh API/env_dev.sh
sh API/runner.sh
#!/bin/bash

chmod 777 -R Docker/redis_dump

docker-compose -f Docker/docker-compose.yml up -d

sh Docker/restore.sh

# sh API/env_dev.sh
# sh API/runner.sh


docker run -i --name api python3:latest -v API:/home/test
docker exec -d api pipenv install Pipfile & pipenv shell & sh runner.sh


docker run -i --name webui python3:latest -v API:/home/test
docker exec -d webui pipenv install Pipfile & pipenv shell & sh runner.sh

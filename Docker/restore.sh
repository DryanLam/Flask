#!/bin/bash

chmod 777 -R redis_dump
docker-compose up -d

docker exec -i mongo-db mongorestore --archive --gzip < mongo_dump.gz
docker exec -i mysql-db /usr/bin/mysql -uroot -pdryan --force tadp < mysql_dump.sql
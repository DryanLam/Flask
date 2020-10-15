#!/bin/bash

docker exec -i mongo-db mongodump --archive --gzip --db tadp > mongo_dump.gz
docker exec mysql-db /usr/bin/mysqldump -uroot -pdryan tadp > mysql_dump.sql

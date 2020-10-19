#!/bin/bash
sudo apt-get install mysql-server
cd /vagrant
pwd
ls -la

chmod 777 -R ./Docker/redis_dump

sh start.sh

docker exec -i mongo-db mongorestore --archive --gzip < ./Docker/mongo_dump.gz

docker ps -a 
sleep 5
docker exec -i mysql-db /usr/bin/mysql -uroot -pdryan --force tadp < ./Docker/mysql_dump.sql


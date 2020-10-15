#!/bin/bash

docker exec -i mysql-db /usr/bin/mysql -uroot -pdryan --force tadp < mysql_dump.sql
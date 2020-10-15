#!/bin/bash

docker exec -i mysql-db /usr/bin/mysql -uroot -pdryan --force tadp < db_dump.sql
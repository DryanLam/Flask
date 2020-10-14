#!/bin/bash

docker exec -i mdb /usr/bin/mysql -uroot -pdryan --force tadp < db_dump.sql
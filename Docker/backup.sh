#!/bin/bash

docker exec mysql-db /usr/bin/mysqldump -uroot -pdryan tadp > db_dump.sql
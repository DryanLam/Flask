#!/bin/bash

docker exec mdb /usr/bin/mysqldump -uroot -pdryan tadp > db_dump.sql
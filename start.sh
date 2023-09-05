#!/bin/bash

if [ -f .env ]
then
    source .env
fi

cp code/db/init.txt code/db/init.sql

sed -i s/MYSQL_DATABASE/$MYSQL_DATABASE/g code/db/init.sql
docker-compose up --build --remove-orphans
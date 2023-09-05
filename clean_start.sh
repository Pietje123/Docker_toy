#!/bin/bash

yes | docker compose down 
yes | docker system prune 
yes | docker volume prune

if [ -f .env ]
then
    set -a
    source .env
    set +a
fi
if [ ! -d  "code/db/sql" ]
then
    mkdir code/db/sql
fi

envsubst < init.txt > code/db/sql/init.sql

docker-compose up --build --remove-orphans
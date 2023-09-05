set -a
source .env
envsubst < init.txt > sql/init.sql
set +a
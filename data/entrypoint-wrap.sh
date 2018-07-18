#!/bin/bash

CQL=`cat schema.sql`

until echo $CQL | cqlsh; do
    echo "cqlsh: Cassandra is unavailable - retry later"
    sleep 2
done &

exec /docker-entrypoint.sh "$@"
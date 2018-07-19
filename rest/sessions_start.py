from flask_restful import Resource
from datetime import datetime, timedelta

from helpers.cassandra import execute


# SELECT * FROM events_start_by_country where ts >= '2016-11-22T20:40:50' ALLOW FILTERING;
class SessionsStart(Resource):
    def get(self, hours):
        hours_ago = datetime.now() - timedelta(hours=hours)
        timestamp = hours_ago.strftime('%Y-%m-%d %H:%M:%S')

        cql = "SELECT * FROM events_start_by_country where ts >= '?' ALLOW FILTERING;"
        return execute(cql, [timestamp])

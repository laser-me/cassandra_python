from flask_restful import Resource
from helpers.cassandra import execute


class SessionsComplete(Resource):
    def get(self, player_id):
        cql = "SELECT * FROM events_complete WHERE player_id='?' LIMIT 20;"
        return execute(cql, [player_id])

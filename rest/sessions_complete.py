from flask import jsonify
from flask_restful import Resource
from helpers.cassandra import execute


class SessionsComplete(Resource):
    def get(self, player_id):
        cql = """SELECT * FROM events_complete WHERE player_id=%s LIMIT 20;"""
        reply = execute(cql, [player_id])

        return jsonify(reply)

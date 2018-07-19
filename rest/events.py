from flask_restful import reqparse, Resource, abort

from helpers.parser import parse_event
from helpers.cassandra import execute

parser = reqparse.RequestParser()
parser.add_argument('events', action='append')


def insert_into_cassandra(event):
    cql = parse_event(event)

    execute(cql)


class Events(Resource):
    def post(self):
        args = parser.parse_args()

        if not args['events']: abort(404, message="No events provided")
        for event in args['events']:
            insert_into_cassandra(event)

        return 'OK', 201

from flask_restful import reqparse, Resource, abort

from helpers.parser import parse_event
from helpers.cassandra import execute

parser = reqparse.RequestParser()
parser.add_argument('events', type=dict, location='json', action='append')


class Events(Resource):
    def post(self):
        args = parser.parse_args()

        cql = "BEGIN BATCH \n"
        if not args['events']: abort(404, message="No events provided")
        for event in args['events']:
            cql = cql + parse_event(event)

        cql = cql + "APPLY BATCH;"
        print(cql)
        execute(cql)
        return 'OK', 201

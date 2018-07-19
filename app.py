from flask import Flask
from flask_restful import Api
from flask_cassandra import CassandraCluster

from rest.events import Events
from rest.sessions_complete import SessionsComplete
from rest.sessions_start import SessionsStart

app = Flask(__name__)
api = Api(app)

app.config['CASSANDRA_NODES'] = ['localhost']  # can be a string or list of nodes
cassandra = CassandraCluster()

api.add_resource(Events, '/events')
api.add_resource(SessionsStart, '/starts/<int:hours>')
api.add_resource(SessionsComplete, '/complete/<string:player_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

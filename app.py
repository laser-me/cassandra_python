from flask import Flask
from flask_restful import Api
from flask_cassandra import CassandraCluster

from rest.events import Events

app = Flask(__name__)
api = Api(app)

app.config['CASSANDRA_NODES'] = ['cassandra']  # can be a string or list of nodes
cassandra = CassandraCluster()

api.add_resource(Events, '/events')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

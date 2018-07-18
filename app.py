from flask import Flask
from flask_cassandra import CassandraCluster

app = Flask(__name__)
cassandra = CassandraCluster()

app.config['CASSANDRA_NODES'] = ['cassandra']  # can be a string or list of nodes

@app.route("/cassandra_test")
def cassandra_test():
    session = cassandra.connect()
    session.set_keyspace("monty_python")
    cql = "SELECT * FROM sketches LIMIT 1"
    r = session.execute(cql)
    return str(r[0])

@app.route("/test")
def test():
    return ('Hello to you', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

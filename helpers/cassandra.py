from flask_cassandra import CassandraCluster

cassandra = CassandraCluster()


def execute(cql, parameters=None):
    session = cassandra.connect()
    session.set_keyspace("a")

    r = session.execute(cql, parameters)

    return str(r[0])

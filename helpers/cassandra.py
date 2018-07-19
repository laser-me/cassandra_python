from flask_cassandra import CassandraCluster

cassandra = CassandraCluster()


def execute(cql):
    session = cassandra.connect()
    session.set_keyspace("a")

    r = session.execute(cql)

    return str(r[0])

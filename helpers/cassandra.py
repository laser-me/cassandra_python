from cassandra.query import dict_factory
from flask_cassandra import CassandraCluster

cassandra = CassandraCluster()


def execute(cql, parameters=None):
    session = cassandra.connect()
    session.row_factory = dict_factory
    session.set_keyspace("a")

    r = session.execute(cql, parameters)

    return r.current_rows

# python converter for jsonl to schema.cql

def convert_data():
    f = open('schema.cql', 'w')

    f.write("CREATE KEYSPACE assignment WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};\n")
    f.write(
        """CREATE TABLE assignment.logs ( \
            player_id text, \
            country text, \
            event text, \
            session_id UUID, \
            ts timestamp, \
            PRIMARY KEY (session_id, ts) \
            );\n""")

    with open("./assignment_data.jsonl") as json_lines:
        for line in json_lines:
            f.write("INSERT INTO assignment.logs JSON '" + line.strip() + "';\n")

    f.close()

if __name__ == '__main__':
    convert_data()

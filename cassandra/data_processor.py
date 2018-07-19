# python converter for jsonl to schema.cql
import json

# limiting big file for testing
limit = None


def convert_data():
    f = open('schema.cql', 'w')

    with open('./base_schema.cql', 'r') as content_file:
        content = content_file.read()
        f.write(content)

        with open("./assignment_data.jsonl") as json_lines:
            count = 0
            for line in json_lines:
                count = count + 1
                if limit and count > limit: break

                json_obj = json.loads(line)

                # actualization of data =)
                timestamp = 0
                cql = ""

                if json_obj['ts']:
                    json_obj['ts'].replace('2016', '2017')

                if json_obj['event'] == 'start':
                    cql = "UPDATE a.events SET ts_start='%(ts)s', country='%(country)s' WHERE player_id='%(player_id)s' AND session_id=%(session_id)s;\n" % json_obj
                    cql += "INSERT INTO a.events_start_by_country JSON '" + json.dumps(json_obj).strip() + "';\n"

                else:
                    cql = "UPDATE a.events SET ts_end='%(ts)s' WHERE player_id='%(player_id)s' AND session_id=%(session_id)s;\n" % json_obj

                f.write(cql)

    f.close()


if __name__ == '__main__':
    convert_data()

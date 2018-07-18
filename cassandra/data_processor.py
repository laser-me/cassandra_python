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
                if json_obj['ts']:
                    json_obj['ts'].replace('2016', '2017')

                if json_obj['event'] == 'start':
                    json_obj['ts_start'] = json_obj['ts']
                else:
                    json_obj['ts_end'] = json_obj['ts']

                del json_obj['event']
                del json_obj['ts']

                f.write("INSERT INTO a.events JSON '" + json.dumps(json_obj).strip() + "';\n")

    f.close()


if __name__ == '__main__':
    convert_data()

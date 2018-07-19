# python converter for jsonl to schema.cql
import json
from helpers.parser import parse_event

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

                if json_obj['ts']:
                    json_obj['ts'].replace('2016', '2017')

                cql = parse_event(json_obj, actualize_time=True)

                f.write(cql)

    f.close()


if __name__ == '__main__':
    convert_data()

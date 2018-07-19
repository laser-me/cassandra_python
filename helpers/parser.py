import json


def parse_event(json_obj, actualize_time=False):
    if actualize_time and json_obj['ts']:
        json_obj['ts'].replace('2016', '2017')

    if json_obj['event'] == 'start':
        cql = "UPDATE a.events SET ts_start='%(ts)s', country='%(country)s' WHERE player_id='%(player_id)s' AND session_id=%(session_id)s;\n" % json_obj
        cql += "INSERT INTO a.events_start_by_country JSON '" + json.dumps(json_obj).strip() + "';\n"

    else:
        cql = "UPDATE a.events SET ts_end='%(ts)s' WHERE player_id='%(player_id)s' AND session_id=%(session_id)s;\n" % json_obj

    return cql

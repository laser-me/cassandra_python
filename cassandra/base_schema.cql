CREATE KEYSPACE IF NOT EXISTS a WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS a.events (
    player_id text,
    country text,
    session_id UUID,
    ts_start timestamp,
    ts_end timestamp,
    PRIMARY KEY (player_id, session_id)
);

CREATE MATERIALIZED VIEW IF NOT EXISTS a.events_by_country AS
    SELECT country, player_id, session_id, ts_start
    FROM a.events
    WHERE ts_start IS NOT NULL AND player_id IS NOT NULL AND session_id IS NOT NULL AND country IS NOT NULL
    PRIMARY KEY (ts_start, player_id, session_id)
    WITH CLUSTERING ORDER BY (ts_start DESC);

CREATE MATERIALIZED VIEW IF NOT EXISTS a.events_complete AS
    SELECT player_id, session_id, ts_start, ts_end, country
    FROM a.events
    WHERE ts_start IS NOT NULL AND ts_end IS NOT NULL AND player_id IS NOT NULL AND session_id IS NOT NULL AND country IS NOT NULL
    PRIMARY KEY ((player_id), ts_end, session_id, country)
    WITH CLUSTERING ORDER BY (ts_end DESC);

CREATE TABLE IF NOT EXISTS a.events_start_by_country (
    player_id text,
    country text,
    event text,
    session_id UUID,
    ts timestamp,
    PRIMARY KEY (country, ts)
) WITH CLUSTERING ORDER BY (ts DESC);
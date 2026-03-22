from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

t_env.execute_sql("""
CREATE TABLE tickets (
    ticket_id STRING,
    created_at TIMESTAMP(3),
    WATERMARK FOR created_at AS created_at - INTERVAL '5' SECOND
) WITH (
    'connector' = 'kafka',
    'topic' = 'tickets_topic',
    'properties.bootstrap.servers' = 'localhost:9092',
    'format' = 'json'
)
""")

result = t_env.sql_query("""
SELECT
    TUMBLE_START(created_at, INTERVAL '1' HOUR) as window_start,
    COUNT(*) as total_tickets
FROM tickets
GROUP BY TUMBLE(created_at, INTERVAL '1' HOUR)
""")

t_env.execute_sql("""
CREATE TABLE sink (
    window_start TIMESTAMP(3),
    total_tickets BIGINT
) WITH ('connector'='print')
""")

result.execute_insert("sink")
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

settings = EnvironmentSettings.in_streaming_mode()
t_env = StreamTableEnvironment.create(env, environment_settings=settings)

# Kafka source
t_env.execute_sql("""
CREATE TABLE products_stream (
    id INT,
    title STRING,
    price DOUBLE,
    category STRING,
    description STRING,
    image STRING
) WITH (
    'connector' = 'kafka',
    'topic' = 'products_stream',
    'properties.bootstrap.servers' = 'localhost:9092',
    'format' = 'json'
)
""")

# Sink (DuckDB vía filesystem / parquet)
t_env.execute_sql("""
CREATE TABLE products_sink (
    id INT,
    title STRING,
    price DOUBLE,
    category STRING
) WITH (
    'connector' = 'filesystem',
    'path' = 'file:///tmp/products_parquet',
    'format' = 'parquet'
)
""")

# Transformación (streaming SQL)
t_env.execute_sql("""
INSERT INTO products_sink
SELECT
    id,
    title,
    price,
    category
FROM products_stream
""")
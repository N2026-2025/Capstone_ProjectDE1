{{ config(materialized='view') }}

select
    date_trunc('day', created_at) as date,
    count(*) as total_tickets
from {{ ref('fact_tickets') }}
group by 1
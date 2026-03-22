{{ config(materialized='view') }}

select
    priority,
    count(*) as total
from {{ ref('fact_tickets') }}
group by priority
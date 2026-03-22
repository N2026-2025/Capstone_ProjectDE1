{{ config(materialized='view') }}

with source as (

    select * from read_parquet('data/bronze/tickets.parquet')

),

cleaned as (

    select
        cast(ticket_id as varchar) as ticket_id,

        cast(customer_id as varchar) as customer_id,
        lower(trim(customer_name)) as customer_name,
        lower(trim(customer_email)) as customer_email,
        cast(customer_age as int) as customer_age,
        lower(trim(gender)) as gender,

        lower(trim(agent)) as agent,
        lower(trim(agent_team)) as agent_team,
        lower(trim(agent_role)) as agent_role,

        cast(product_id as varchar) as product_id,
        lower(trim(product_name)) as product_name,

        cast(created_at as timestamp) as created_at,
        cast(resolved_at as timestamp) as resolved_at,

        cast(first_response_time as double) as first_response_time,
        cast(time_to_resolution as double) as time_to_resolution,

        cast(customer_satisfaction_rating as double) as customer_satisfaction_rating,

        lower(trim(status)) as status,
        lower(trim(priority)) as priority

    from source

)

select * from cleaned
SELECT 
    ticket_id,
    customer_id,
    LOWER(category) as category,
    cac,
    revenue,
    nps_score,
    CAST(created_at AS TIMESTAMP) as created_at,
    CAST(closed_at AS TIMESTAMP) as closed_at
FROM {{ source('raw', 'tickets') }}

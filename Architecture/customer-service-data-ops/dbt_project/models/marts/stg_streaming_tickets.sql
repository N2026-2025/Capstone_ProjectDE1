{{ config(materialized='incremental', unique_key='ticket_id') }}

SELECT * FROM {{ ref('stg_streaming_tickets') }}
{% if is_incremental() %}
  -- Solo procesa lo nuevo, pero mira 3 horas atrás por si hubo lag
  WHERE event_timestamp >= (select max(event_timestamp) from {{ this }}) - interval '3 hours'
{% endif %}
#3. Pensamiento Adelantado: El problema del "Late Arriving Data"
#Un problema futuro común es que un log de streaming llegue 2 horas tarde por un fallo de red.
#Solución en Código (dbt Incremental)

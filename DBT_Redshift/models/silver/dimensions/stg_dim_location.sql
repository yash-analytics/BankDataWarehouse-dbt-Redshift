{{
    config(
        materialized='incremental',
        alias='stg_dim_location',
        schema=var('silver_schema'),
        unique_key='location_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    location_id,
    city,
    state,
    country,
    postal_code,
    getdate() as created_at
FROM
    {{ var('bronze_schema') }}.locations
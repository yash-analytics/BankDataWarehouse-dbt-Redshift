{{
    config(
        materialized='incremental',
        alias='dim_customer',
        schema=var('gold_schema'),
        unique_key='customer_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    customer_id,
    first_name,
    last_name,
    full_name,
    email,
    address,
    city,
    state,
    postal_code,
    phone_number,
    created_at
FROM
    {{ ref('stg_dim_customer') }}
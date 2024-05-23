{{
    config(
        materialized='incremental',
        alias='stg_dim_customer',
        schema=var('silver_schema'),
        unique_key='customer_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    customer_id,
    first_name,
    last_name,
    concat(concat(first_name, ' '), last_name) as full_name,
    email,
    address,
    city,
    state,
    postal_code,
    phone_number,
    getdate() as created_at
FROM
    {{ var('bronze_schema') }}.customers
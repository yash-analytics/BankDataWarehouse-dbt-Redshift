{{
    config(
        materialized='incremental',
        alias='stg_dim_currency',
        schema=var('silver_schema'),
        unique_key='currency_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    currency_id,
    currency_code,
    currency_name,
    getdate() as created_at
FROM
    {{ var('bronze_schema') }}.currencies
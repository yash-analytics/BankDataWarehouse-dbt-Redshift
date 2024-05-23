{{
    config(
        materialized='incremental',
        alias='stg_dim_transaction_type',
        schema=var('silver_schema'),
        unique_key='transaction_type_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    transaction_type_id,
    transaction_type_name,
    getdate() as created_at
FROM
    {{ var('bronze_schema') }}.transaction_types
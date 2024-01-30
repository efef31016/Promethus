# ETL Monitor

This monitoring API can be integrated into various scenarios in airflow; first, imitate the execution sequence of 'Monitor.py' to use it. (Of course, you can fix the response to show system info by modifying 'ResponseFormat.py')

### Definition of Format
- Key (Pure Text) - Value (Float32)
- 'key-value' (same as parameters)
- value Definition:
  - `0.0`: Success,
  - `1.0`: Failure, need alert
  - Suffix with `num_`: fail number

- Prefix Definition (default: True):
  - `empty_check_`(1.0): 資料庫是否為空，空則告警
  - `lose_check_XXX_`(1.0): 資料是否有少，有則告警 
  - `lose_check_XXX_num_`(0.0): 缺少的筆數

### Promethus Response
For example:
| Metric Key                                | Value | Meaning            |
|-------------------------------------------|-------|--------------------|
| empty_check_www_XXXXXX_XXX                | 0.0   | Success            |
| lose_check_customer_www_XXXXXX_XXX        | 1.0   | Failure, Alert     |
| lose_check_customer_fail_num_www_XXXX_XXX | 0.0   | Success            |
| lose_check_order_www_XXXXXX_XXX           | 1.0   | Failure, Alert     |
| lose_check_order_fail_num_www_XXXXXX_XXX  | 0.0   | Success            |
| lose_check_product_www_XXXXXX_XXX         | 1.0   | Failure, Alert     |
| lose_check_product_fail_num_www_XXXXX_XXX | 0.0   | Success            |
| empty_check_www_XXXXXXXX_XXXXXX           | 0.0   | Success            |
| lose_check_customer_www_XXXXXXXX_XXXXXX   | 1.0   | Failure, Alert     |
| lose_check_customer_fail_num_www_XXXXX_XX | 0.0   | Success            |
| lose_check_order_www_XXXXXXX_XXXXXXX      | 1.0   | Failure, Alert     |
| lose_check_order_fail_num_www_XXXXXXXX_XX | 0.0   | Success            |
| lose_check_product_www_XXXXXXXXX_XXXXX    | 1.0   | Failure, Alert     |
| lose_check_product_fail_num_www_XXXXX_XXX | 0.0   | Success            |

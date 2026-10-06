# Synthetic Data Catalog

All records are synthetic. The data intentionally contains realistic variation, edge cases, limited missingness, inconsistent legacy classifications and selected integrity anomalies for discovery and transformation exercises.

## `alerts.csv`
- Rows: 1,800
- Columns: `alert_id`, `customer_id`, `alert_type`, `severity`, `status`, `source`, `owner`, `score`

## `applications.csv`
- Rows: 5,000
- Columns: `application_id`, `customer_id`, `product`, `amount`, `currency`, `status`, `credit_score`, `decision_source`, `channel`, `application_date`

## `baseline_metrics.csv`
- Rows: 180
- Columns: `date`, `work_items`, `avg_cycle_minutes`, `manual_effort_hours`, `error_rate_pct`, `exception_rate_pct`, `estimated_cost_units`

## `beneficiaries.csv`
- Rows: 1,200
- Columns: `beneficiary_id`, `customer_id`, `name`, `country`, `bank_code`, `risk_flag`

## `customers.csv`
- Rows: 3,500
- Columns: `customer_id`, `first_name`, `full_name`, `city`, `segment`, `age`, `email`, `phone`, `risk_band`, `pep_flag`

## `kyc_cases.csv`
- Rows: 1,200
- Columns: `kyc_case_id`, `customer_id`, `status`, `document_type`, `verification_source`, `age_days`

## `repayments.csv`
- Rows: 5,000
- Columns: `repayment_id`, `application_id`, `customer_id`, `amount`, `status`, `days_past_due`

## `transactions.csv`
- Rows: 9,000
- Columns: `transaction_id`, `customer_id`, `amount`, `currency`, `direction`, `rail`, `status`, `txn_date`

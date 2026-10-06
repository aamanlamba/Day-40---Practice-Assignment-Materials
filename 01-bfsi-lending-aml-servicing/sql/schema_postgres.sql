-- PostgreSQL-oriented brownfield baseline. Some ETL jobs still bypass these tables.

CREATE SCHEMA IF NOT EXISTS ops;

CREATE TABLE IF NOT EXISTS ops.ingestion_log (id BIGSERIAL PRIMARY KEY, source_file TEXT NOT NULL, row_count INTEGER, loaded_at TIMESTAMPTZ DEFAULT now(), status TEXT);

CREATE TABLE IF NOT EXISTS ops.customers_raw (row_id BIGSERIAL PRIMARY KEY, payload JSONB NOT NULL, source_file TEXT, loaded_at TIMESTAMPTZ DEFAULT now());

CREATE TABLE IF NOT EXISTS ops.applications_raw (row_id BIGSERIAL PRIMARY KEY, payload JSONB NOT NULL, source_file TEXT, loaded_at TIMESTAMPTZ DEFAULT now());

CREATE TABLE IF NOT EXISTS ops.transactions_raw (row_id BIGSERIAL PRIMARY KEY, payload JSONB NOT NULL, source_file TEXT, loaded_at TIMESTAMPTZ DEFAULT now());

CREATE TABLE IF NOT EXISTS ops.alerts_raw (row_id BIGSERIAL PRIMARY KEY, payload JSONB NOT NULL, source_file TEXT, loaded_at TIMESTAMPTZ DEFAULT now());

CREATE TABLE IF NOT EXISTS ops.repayments_raw (row_id BIGSERIAL PRIMARY KEY, payload JSONB NOT NULL, source_file TEXT, loaded_at TIMESTAMPTZ DEFAULT now());

CREATE TABLE IF NOT EXISTS ops.legacy_staging (source_file TEXT, raw_line TEXT, load_ts TIMESTAMPTZ DEFAULT now());

CREATE INDEX IF NOT EXISTS idx_ingestion_source ON ops.ingestion_log(source_file);

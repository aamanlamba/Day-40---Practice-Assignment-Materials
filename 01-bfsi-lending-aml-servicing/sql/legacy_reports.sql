-- Inherited reports intentionally retain legacy patterns and should be assessed before reuse.
SELECT * FROM ops.legacy_staging WHERE raw_line IS NOT NULL;
SELECT source_file, count(*) AS lines FROM ops.legacy_staging GROUP BY source_file ORDER BY lines DESC;

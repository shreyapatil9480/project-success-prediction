-- Stakeholder summary metrics for D01
SELECT
  COUNT(*) AS total_records,
  AVG(CAST(roi_positive AS FLOAT)) AS roi_positive_rate
FROM campaign_performance;

SELECT *
FROM campaign_performance
ORDER BY 1
LIMIT 10;

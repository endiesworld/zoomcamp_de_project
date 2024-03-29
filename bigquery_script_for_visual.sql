-- Create a new table that contains only cycling data for december 2022
CREATE OR REPLACE TABLE `dtc-de-course-01-2024.uk_cycling_data.dec_2022_journey_filtered` AS
SELECT *
FROM `dtc-de-course-01-2024.uk_cycling_data.dec_2022_journey`
WHERE start_date BETWEEN '2022-12-01 00:00:00' AND '2022-12-31 23:59:59'
  AND end_date BETWEEN '2022-12-01 00:00:00' AND '2022-12-31 23:59:59';


-- Bikes and total time traveled 
SELECT
  bike_number,bike_model, SUM(total_duration_ms) AS total_journey_time
FROM  `dtc-de-course-01-2024.uk_cycling_data.dec_2022_journey`
GROUP BY bike_number, bike_model 
ORDER BY total_journey_time DESC;
-- Click on Explore Data Icon at the buttom right and click on Explore with looker studio, to visualize the result.
-- Report link: https://lookerstudio.google.com/s/pjSs0CwvXjk


-- Busiest stations by bike count
WITH station_counts AS (
    SELECT station, COUNT(*) AS total_count
    FROM (
        SELECT start_station AS station FROM `dtc-de-course-01-2024.uk_cycling_data.dec_2022_journey`
        UNION ALL
        SELECT end_station AS station FROM `dtc-de-course-01-2024.uk_cycling_data.dec_2022_journey`
    ) AS all_stations
    GROUP BY station
)

SELECT station, total_count
FROM station_counts
ORDER BY total_count DESC;
-- Click on Explore Data Icon at the buttom right and click on Explore with looker studio, to visualize the result.
-- Report link: https://lookerstudio.google.com/s/sZFMRm2O078


-- Daily trip count Dec. 2022
SELECT
  DATE(start_date) AS trip_day,
  COUNT(*) AS trip_count
FROM
  `dtc-de-course-01-2024.uk_cycling_data.dec_2022_journey`
WHERE
  EXTRACT(MONTH FROM start_date) = 12
GROUP BY
  trip_day
ORDER BY
  trip_day;
-- Click on Explore Data Icon at the buttom right and click on Explore with looker studio, to visualize the result.
-- Report link: https://lookerstudio.google.com/s/g_Hia0ZXJ9M



-- Scriot that rank country origin ordered by the numbers of non-unique
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

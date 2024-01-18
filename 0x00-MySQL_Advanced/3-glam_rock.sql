-- Script that lists all bands with Glam rock as their main style, ranked by their longevity
-- column name band_name and lifespan
-- formed and split for computing lifespan

SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
FROM metal_bands
WHERE style LIKE  '%Glam rock%'
ORDER BY lifespan DESC; 


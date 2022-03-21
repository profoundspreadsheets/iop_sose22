/* JSON Query 1 */
SELECT plane.registration, 
plane.livery, 
barunit.unitid,
barunit.cost,
barunit.features,
beverage.bottleid,
beverage.beveragetype 
FROM plane 
INNER JOIN barunit ON plane.registration=barunit.registration 
INNER JOIN beverage ON barunit.unitid=beverage.unitid
WHERE plane.livery='eurowhite';

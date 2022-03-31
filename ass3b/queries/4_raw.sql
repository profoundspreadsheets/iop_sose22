/* DONE JSON 1 */
SELECT plane.registration, 
plane.color,
barunit.unitid,
barunit.teamid,
barunit.features,
beverage.beveragetype,
beverage.cost
FROM plane 
INNER JOIN barunit ON plane.registration=barunit.registration 
INNER JOIN beverage ON barunit.unitid=beverage.unitid
WHERE plane.livery='eurowhite';

/* DONE JSON 1 */
\copy (SELECT plane.registration, 
plane.color,
barunit.unitid,
barunit.teamid,
barunit.features,
beverage.beveragetype,
beverage.cost
FROM plane 
INNER JOIN barunit ON plane.registration=barunit.registration 
INNER JOIN beverage ON barunit.unitid=beverage.unitid
WHERE plane.livery='eurowhite') TO '/home/paul/Dokumente/iop_sose22/ass3a/querieswithcopy/rawoutput/4_rawout.txt';

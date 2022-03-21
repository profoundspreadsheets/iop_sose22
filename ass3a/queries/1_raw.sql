/* DONE XML 1*/
SELECT manufacturingteam.teamid, 
manufacturingteam.employees, 
barunit.unitid,
barunit.registration,
plane.Wingtips,
plane.NumWindows,
plane.seatconfig
FROM manufacturingteam 
INNER JOIN barunit ON manufacturingteam.teamid=barunit.teamid 
INNER JOIN plane ON barunit.registration=plane.registration 
WHERE employees<4;

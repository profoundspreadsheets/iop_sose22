/* DONE XML 1*/
\copy (SELECT manufacturingteam.teamid, 
manufacturingteam.employees, 
barunit.unitid,
barunit.registration,
plane.Wingtips,
plane.NumWindows,
plane.seatconfig
FROM manufacturingteam 
INNER JOIN barunit ON manufacturingteam.teamid=barunit.teamid 
INNER JOIN plane ON barunit.registration=plane.registration 
WHERE employees<4) TO '/home/paul/Dokumente/iop_sose22/ass3a/querieswithcopy/rawoutput/1_rawout.txt';

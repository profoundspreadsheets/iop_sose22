SELECT manufacturingteam.teamid, 
employees, 
country.iso_code, 
tariff, 
cost, 
toiletunit.unitid, 
unitvolume, 
unitweight, 
toiletspecs 
FROM manufacturingteam 
INNER JOIN country ON manufacturingteam.iso_code=country.iso_code 
INNER JOIN toiletunit ON manufacturingteam.teamid=toiletunit.teamid 
WHERE employees<4;

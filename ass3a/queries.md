## manufacturingteam -> country -> toiletunit
### Count
SELECT count(manufacturingteam.teamid) from manufacturingteam WHERE employees<4;
### Query
SELECT manufacturingteam.teamid, employees, country.iso_code, tariff, cost, toiletunit.unitid, unitvolume, unitweight, toiletspecs FROM manufacturingteam INNER JOIN country ON manufacturingteam.iso_code=country.iso_code INNER JOIN toiletunit ON manufacturingteam.teamid=toiletunit.teamid WHERE employees<4;

## plane -> customer -> toiletunit
### Count
SELECT count(plane.registration) from plane WHERE color='white';
### Query
SELECT plane.registration, plane.color, customer.firstname, customer.lastname, plane.seatconfig, toiletunit.unitid, toiletunit.cost FROM plane INNER JOIN customer ON plane.customerid=customer.customerid INNER JOIN toiletunit ON plane.registration=toiletunit.registration WHERE plane.color='white';

## plane -> barunit -> beverage
### Count
SELECT count(plane.livery) from plane WHERE livery='eurowhite';
### Query
SELECT plane.registration, plane.livery, barunit.unitid, barunit.cost, barunit.features, beverage.bottleid, beverage.beveragetype FROM plane INNER JOIN barunit ON plane.registration=barunit.registration INNER JOIN beverage ON barunit.unitid=beverage.unitid WHERE plane.livery='eurowhite';

## plane -> testprotocol -> customer
### Count
SELECT count(plane.registration) from plane WHERE livery='cheatline';
### Query
SELECT plane.registration, plane.livery, testprotocol.testdate, testprotocol.results, testprotocol.pilot, customer.customerid, customer.firstname, customer.lastname FROM plane INNER JOIN testprotocol ON plane.registration=testprotocol.registration INNER JOIN customer ON plane.customerid=customer.customerid WHERE plane.livery='cheatline';
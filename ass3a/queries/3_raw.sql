/* JSON Query 1 */
SELECT plane.registration, plane.color, 
customer.firstname, customer.lastname,
customer.street,
customer.housenumber,
customer.zip,
customer.city,
toiletunit.unitid, toiletunit.toiletspecs
FROM plane 
INNER JOIN customer ON plane.customerid=customer.customerid 
INNER JOIN toiletunit ON plane.registration=toiletunit.registration 
WHERE plane.livery='eurowhite';

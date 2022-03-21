SELECT plane.registration, plane.color, customer.firstname, customer.lastname, plane.seatconfig, toiletunit.unitid, toiletunit.cost 
FROM plane 
INNER JOIN customer ON plane.customerid=customer.customerid 
INNER JOIN toiletunit ON plane.registration=toiletunit.registration 
WHERE plane.livery='eurowhite';

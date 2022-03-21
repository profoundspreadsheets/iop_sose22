/* DONE JSON 1*/
\copy (SELECT plane.registration, 
customer.firstname, 
customer.lastname,
customer.street,
customer.housenumber,
customer.zip,
customer.city,
toiletunit.unitid, 
toiletunit.toiletspecs
FROM plane 
INNER JOIN customer ON plane.customerid=customer.customerid 
INNER JOIN toiletunit ON plane.registration=toiletunit.registration 
WHERE plane.livery='eurowhite') TO '/home/paul/Dokumente/iop_sose22/ass3a/querieswithcopy/rawoutput/3_rawout.txt;

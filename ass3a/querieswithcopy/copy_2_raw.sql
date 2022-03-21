/* DONE XML 1*/
\copy (SELECT customer.customerid, 
customer.firstname, 
customer.lastname, 
plane.registration, 
testprotocol.protocolid, 
testprotocol.testdate, 
testprotocol.results
FROM plane 
INNER JOIN testprotocol ON plane.registration=testprotocol.registration 
INNER JOIN customer ON plane.customerid=customer.customerid 
WHERE plane.livery='cheatline') TO '/home/paul/Dokumente/iop_sose22/ass3a/querieswithcopy/rawoutput/2_rawout.txt';

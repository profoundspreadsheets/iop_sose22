/* DONE XML 1*/
\copy (SELECT xmlroot(
    XMLELEMENT(NAME "Customers",
        XMLAGG(
            XMLELEMENT(NAME "Customer",
                XMLATTRIBUTES(
                    customer.customerid AS "customerid"
                ),
                XMLFOREST(
                    customer.firstname AS "Firstname",
                    customer.lastname AS "Lastname"
                ),
                XMLELEMENT(NAME "Planes",
                    (SELECT XMLAGG(
                        XMLELEMENT(NAME "Plane",
                            XMLATTRIBUTES(
                                plane.registration AS "registration"
                            ),
                            XMLELEMENT(NAME "Protocols",
                                (SELECT XMLAGG(
                                    XMLELEMENT(NAME "Protocol",
                                        XMLATTRIBUTES(
                                            testprotocol.ProtocolId AS "protocolid"
                                        ),
                                        XMLELEMENT(NAME "Testdate", testprotocol.testdate),
                                        testprotocol.results
                                    )
                                ) FROM testprotocol
                                WHERE testprotocol.registration = plane.registration)
                            )
                        )
                    ) FROM plane
                    WHERE plane.customerid = customer.customerid AND plane.livery='cheatline')
                )
            )
        )
    ), version '1.0', standalone yes
) FROM plane 
INNER JOIN customer ON plane.customerid = customer.customerid
WHERE plane.livery='cheatline')
TO '/home/paul/Documents/iop_sose22/ass3c/xmls/2_data.xml';
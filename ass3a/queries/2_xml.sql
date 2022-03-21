\copy (SELECT xmlroot(
    XMLELEMENT(NAME "Planes",
        XMLAGG(
            XMLELEMENT( NAME "Plane",
                XMLATTRIBUTES(
                    plane.registration AS "registration"
                ),
                XMLELEMENT( NAME "Customer", 
                    XMLFOREST(
                        customer.firstname AS "Firstname",
                        customer.lastname AS "Lastname"
                    ),
                    XMLELEMENT( NAME "Address",
                        XMLATTRIBUTES(
                            customer.zip AS "zip",
                            customer.City AS "City"
                        ),
                        XMLFOREST(
                            customer.street AS "Street",
                            customer.Housenumber AS "Housenumber"
                        )
                    )
                ),
                XMLELEMENT( NAME "Toilets",
                    (SELECT XMLAGG(
                        XMLELEMENT( NAME "ToiletSpecs",
                            XMLATTRIBUTES(
                                toiletunit.unitid AS "unitid"
                            ),
                            XMLFOREST(
                                toiletunit.toiletspecs -> 'toiletunit-specs' ->> 'capacity' AS "Capacity",
                                toiletunit.toiletspecs -> 'toiletunit-specs' ->> 'flowrate' AS "Flowrate"
                            )
                        )
                    ) FROM toiletunit
                    WHERE plane.registration = toiletunit.registration)
                )
            )
        )
),
version '1.0', standalone yes)
FROM plane INNER JOIN customer ON plane.customerid=customer.customerid INNER JOIN toiletunit ON plane.registration=toiletunit.registration
WHERE plane.livery='eurowhite') TO '/home/paul/Dokumente/iop_sose22/ass3a/xmls/2_data.xml';
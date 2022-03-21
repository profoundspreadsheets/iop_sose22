/* JSON Query 2 */
\copy (SELECT xmlroot(
    XMLELEMENT(NAME "Planes",
        XMLAGG(
            XMLELEMENT(NAME "Plane",
                XMLATTRIBUTES(
                    plane.registration AS "registration"
                ),
                XMLELEMENT(
                    NAME "Bars",
                    (SELECT XMLAGG(
                        XMLELEMENT(NAME "Bar",
                            XMLATTRIBUTES(
                                barunit.unitid AS "unitid",
                                barunit.TeamId AS "teamid"
                            ),
                            XMLELEMENT(NAME "Minifridges",
                                XMLFOREST(
                                    barunit.features -> 'barunit-features' -> 'minifridges' ->> 'amount' AS "Amount"
                                )
                            ),
                            XMLELEMENT(NAME "Glasses",
                                XMLFOREST(
                                    barunit.features -> 'barunit-features' -> 'glasses' ->> 'type' AS "Type",
                                    barunit.features -> 'barunit-features' -> 'glasses' ->> 'amount' AS "Amount"
                                )
                            ),
                            XMLELEMENT(NAME "Beverages",
                                (SELECT XMLAGG(
                                    XMLELEMENT(NAME "Beverage",
                                        XMLFOREST(
                                            beverage.beveragetype AS "Drink",
                                            beverage.cost AS "Cost"
                                        )
                                    )
                                ) FROM beverage
                                WHERE beverage.unitid = barunit.unitid)
                            )
                        )
                    ) FROM barunit
                    WHERE plane.registration = barunit.registration)
                )
            )
        )
), 
version '1.0', standalone yes)
FROM plane 
INNER JOIN barunit ON plane.registration=barunit.registration 
INNER JOIN beverage ON barunit.unitid=beverage.unitid
WHERE plane.livery='eurowhite') TO '/home/paul/Dokumente/iop_sose22/ass3a/xmls/4_data.xml';
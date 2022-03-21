/* DONE XML 1 */
\copy (SELECT xmlroot(
    XMLELEMENT(NAME "Teams",
        XMLAGG(
            XMLELEMENT(NAME "Team",
                XMLATTRIBUTES(
                    manufacturingteam.teamid AS "teamid",
                    manufacturingteam.employees AS "employees"
                ),
                XMLELEMENT(NAME "Units", 
                (SELECT XMLAGG(
                    XMLELEMENT(NAME "Unit", 
                        XMLATTRIBUTES(
                            barunit.unitid AS "unitid",
                            barunit.registration AS "registration"
                        ),
                        XMLFOREST(
                            plane.Wingtips AS "Wingtips",
                            plane.NumWindows AS "Windows"
                        ),
                        (SELECT plane.seatconfig FROM plane WHERE plane.registration=barunit.registration)
                    )
                ) FROM barunit
                WHERE barunit.teamid = manufacturingteam.teamid)
                )
            )
        )
    ), version '1.0', standalone yes
) FROM manufacturingteam 
INNER JOIN barunit ON barunit.teamid=manufacturingteam.teamid
INNER JOIN plane ON plane.registration=barunit.registration
WHERE employees<4) TO '/home/paul/Dokumente/iop_sose22/ass3a/xmls/1_data.xml';

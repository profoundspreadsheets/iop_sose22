\copy (SELECT xmlroot(
    XMLELEMENT(NAME "Teams",
        XMLAGG(
            XMLELEMENT(NAME "Team",
                XMLATTRIBUTES(
                    manufacturingteam.teamid AS "teamid",
                    manufacturingteam.employees AS "employees"
                ),
                XMLFOREST(
                    manufacturingteam.ISO_Code AS "ISO_Code",
                    manufacturingteam.HourlyRate AS "HourlyRate"
                ),
                XMLELEMENT(NAME "Units", 
                (SELECT XMLAGG(
                    XMLELEMENT(NAME "Unit", 
                        XMLATTRIBUTES(
                            barunit.unitid AS "unitid",
                            barunit.registration AS "registration"
                        ),
                        XMLELEMENT(NAME "Wingtips",
                            (SELECT plane.Wingtips FROM plane WHERE plane.registration=barunit.registration)    
                        ),
                        XMLELEMENT(NAME "Windows",
                            (SELECT plane.NumWindows FROM plane WHERE plane.registration=barunit.registration)    
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
WHERE employees<4) TO '/home/paul/Documents/iop_sose22/ass5/fixedXMLs/1_data.xml';

let $doc4:=doc("./4_data.xml")
    for $manufacturingteam in $doc4/customers/customer/companies/company/manufacturingteams/manufacturingteam
    return <Team teamid="{data($manufacturingteam/@manufacturingteamid)}" employees="0">
        <Units/> 
    </Team>
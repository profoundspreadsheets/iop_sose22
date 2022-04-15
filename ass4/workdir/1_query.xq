<Teams>{
    let $doc2:=doc("./2_data.xml")
    for $manufacturingteam in $doc2/manufacturingteams/manufacturingteam
    return <Team teamid="{data($manufacturingteam/manufacturingteamid)}" employees="0">
        <Units>
            {
                for $airplane in $manufacturingteam/airplanes/airplane
                return
                    <Unit unitid="DEFAULT" registration="{data($airplane/@serialNumber)}">
                        <Wingtips>True</Wingtips>
                        <Windows>4</Windows>
                        <seatconfig>
                            <brand name="Recaro"/>
                        </seatconfig>
                    </Unit>
            }
        </Units>
    </Team>
}
{
    let $doc4:=doc("./4_data.xml")
    for $manufacturingteam in $doc4/customers/customer/companies/company/manufacturingteams/manufacturingteam
    return <Team teamid="{data($manufacturingteam/@manufacturingteamid)}" employees="0">
        <Units/> 
    </Team>
}
</Teams>
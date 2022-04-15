<Teams>{
    let $doc2:=doc("./2_data.xml")
    for $manufacturingteam in $doc2/manufacturingteams/manufacturingteam
    return <Team teamid="{data($manufacturingteam/manufacturingteamid)}" employees="0">
        <Units>{
            let $unit:=
            if (exists($manufacturingteam/airplanes/airplane)) then (
                <Unit unitid="DEFAULT" registration="{data($manufacturingteam/airplanes/airplane/@serialNumber)}">
                    <Wingtips>True</Wingtips>
                    <Windows>4</Windows>
                    <seatconfig>
                        <brand>Recaro</brand>
                    </seatconfig>
                </Unit> ) else (
                    <Unit unitid="DEFAULT" registration="DEFAULT">
                        <seatconfig>
                            <brand>Recaro</brand>
                        </seatconfig>
                    </Unit>
                )
            return $unit
        }</Units>
    </Team>
}
{
    let $doc4:=doc("./4_data.xml")
    for $manufacturingteam in $doc4/customers/customer/companies/company/manufacturingteams/manufacturingteam
    return <Team teamid="{data($manufacturingteam/@manufacturingteamid)}" employees="0">
        <Units> 
            <Unit unitid="DEFAULT" registration="DEFAULT">
                <seatconfig>
                    <brand>Recaro</brand>
                </seatconfig>
            </Unit>
        </Units>
    </Team>
}
</Teams>
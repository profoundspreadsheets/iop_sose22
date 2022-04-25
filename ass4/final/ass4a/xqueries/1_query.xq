<Teams>{
    let $doc2:=doc("./2_data.xml")
    for $manufacturingteam in $doc2/manufacturingteams/manufacturingteam
    let $teamsize := data($manufacturingteam/manufacturingteamaddress/address/address/street/number[./@type="staircase"])
    return <Team teamid="{data($manufacturingteam/manufacturingteamid)}" employees="{$teamsize}">
        <Units>{
            let $teamname := data($manufacturingteam/manufacturingteamname)
            let $teamcity := data($manufacturingteam/manufacturingteamaddress/address/address/city)
            let $unitid_ := concat($teamname, $teamcity)
            let $unit:=
            if (exists($manufacturingteam/airplanes/airplane)) then (
                <Unit unitid="{$unitid_}" registration="{data($manufacturingteam/airplanes/airplane/@serialNumber)}">
                    <Wingtips>True</Wingtips>
                    <Windows>4</Windows>
                    <seatconfig>
                        <seat compartment="business" cover="fabric">
                            <amount>2</amount>
                            <tv/>
                        </seat>
                        <brand>Recaro</brand>
                    </seatconfig>
                </Unit> ) else (
                    <Unit unitid="{$unitid_}" registration="No plane">
                        <seatconfig>
                            <seat compartment="business" cover="fabric">
                                <amount>2</amount>
                                <tv/>
                            </seat>
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
    (: employees calculated by companyId floor division by 40 :)
    return <Team teamid="{data($manufacturingteam/@manufacturingteamid)}" employees="{fn:floor($manufacturingteam/ancestor::company/@companyId div 40)}">
        <Units>{
            let $teamname := data($manufacturingteam/manufacturingteamname)
            let $teamid := data($manufacturingteam/@manufacturingteamid)
            let $unitid_ := concat($teamname, '_', $teamid)
            return
            <Unit unitid="{$unitid_}" registration="No plane">
                <seatconfig>
                    <seat compartment="business" cover="fabric">
                        <amount>2</amount>
                        <tv/>
                    </seat>
                    <brand>Recaro</brand>
                </seatconfig>
            </Unit>
        }</Units>
    </Team>
}
</Teams>
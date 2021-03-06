<Planes>{
    let $doc4:=doc("./4_data.xml")
    for $customer in $doc4//customer
    return <Plane registration="{index-of($doc4//customer, $customer)}">
        <Customer>
        <Firstname>{data($customer/firstname)}</Firstname>
        <Lastname>{data($customer/surname)}</Lastname>
        </Customer>
        <Toilets>{
        if (exists($customer/companies/company)) then (
            <ToiletSpecs unitid="{data($customer/companies/company/@companyId)}">
            <Capacity>{data(fn:round(xs:double($customer/companies/company[1]/@companyId div 80),2))}</Capacity>
            <Flowrate>{data(fn:round(xs:double($customer/companies/company[1]/@companyId div 320),2))}</Flowrate>
            </ToiletSpecs>
        )
        else (
            (: fallback toilet :)
            <ToiletSpecs unitid="UUID">
                <Capacity>10.0</Capacity>
                <Flowrate>2.0</Flowrate>
            </ToiletSpecs>)
        }</Toilets>
    </Plane>
}</Planes>
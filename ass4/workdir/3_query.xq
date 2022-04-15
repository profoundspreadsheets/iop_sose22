<Planes>{
    let $doc4:=doc("./4_data.xml")
    for $customer in $doc4//customer
    return <Plane registration="{index-of($doc4//customer, $customer)}">
        <Customer>
        <Firstname>{data($customer/firstname)}</Firstname>
        <Lastname>{data($customer/surname)}</Lastname>
        <Toilets>
            <Toilet>
                <toiletspecs unitid="Insert UUID here">
                    <Capacity>10.0</Capacity>
                    <Flowrate>2.0</Flowrate>
                </toiletspecs>
            </Toilet>
        </Toilets>
        </Customer>
    </Plane>
}</Planes>
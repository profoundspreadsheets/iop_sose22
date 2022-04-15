<Customers>{
    let $doc1:=doc("./1_data.xml")
    for $company in $doc1//companies/company
    return 
        if(exists($company/customers/customer)) then (    
            <Customer customerid="{data($company/customers/customer/@customerId)}">
                <Firstname>{data($company/customers/customer/firstname)}</Firstname>
                <Lastname>{data($company/customers/customer/surname)}</Lastname>
                <Planes>
                    {
                        let $doc3:=doc("./3_data.xml")
                        let $indexCurrComp:=index-of($doc1//companies/company, $company)
                        let $plane:=$doc3//airplane[$indexCurrComp]
                        return <Plane registration="{$plane/serialnumber}">
                            <Protocols>{
                                for $protocol in $plane/flighttests/flighttest
                                return
                                <Protocol protocolid="{data($protocol/@testId)}">
                                    <Testdate>{data($protocol/testdate)}</Testdate>
                                    <results/>
                                </Protocol>
                            }
                            </Protocols>
                        </Plane>
                    }
                </Planes>
            </Customer>)
        else ()
}</Customers>
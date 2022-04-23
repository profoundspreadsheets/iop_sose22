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
                                for $protocol in $plane/flighttests/flighttest/testprotocols/testprotocol
                                let $critical_:=data($protocol/improvementmandatory)
                                return
                                <Protocol protocolid="{data($protocol/@testprotocolid)}">
                                    <Testdate>{data($protocol/ancestor::flighttest/testdate/text())}</Testdate>
                                    <results>
                                        <test>wings</test>
                                        <vibrations loc="DEFAULT">
                                            <scale/>
                                            <critical>{xs:boolean($critical_)}</critical>
                                        </vibrations>
                                        <detached-wing side="left">false</detached-wing>
                                        <detached-wing side="right">false</detached-wing>
                                    </results>
                                </Protocol>
                            }
                            </Protocols>
                        </Plane>
                    }
                </Planes>
            </Customer>)
        else ()
}</Customers>
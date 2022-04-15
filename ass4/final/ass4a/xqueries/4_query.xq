<Planes>{
    let $doc3:=doc("./3_data.xml")
    for $airplane in $doc3/airplanes/airplane
    return 
        <Plane registration="{data($airplane/serialnumber)}">
            <Color>White</Color>
            <Livery>eurowhite</Livery>
            <Bars/>
        </Plane>
}</Planes>
<?php
class Server {
  function sxml_append(SimpleXMLElement $to, SimpleXMLElement $from) {
    $toDom = dom_import_simplexml($to);
    $fromDom = dom_import_simplexml($from);
    $toDom->appendChild($toDom->ownerDocument->importNode($fromDom, true));
  }

  //xpath11.xp
  function getTeamsByEmployees($numEmployees) {
    $xml = simplexml_load_file("1_data.xml");
    $returnXML = new SimpleXMLElement('<Teams></Teams>');    
    $query = "//Team[@employees <= $numEmployees]";
    $result = $xml->xpath($query);
    foreach ($result as $node) {
      $this->sxml_append($returnXML, $node);
    }
    return $returnXML->asXML();
  }

  //xpath12.xp
  function getTeamsByCountry($countryCodes) {
    $xml = simplexml_load_file("1_data.xml");
    $returnXML = new SimpleXMLElement('<Teams></Teams>');    
    foreach ($countryCodes->country as $country) {
      $query = "//ISO_Code[.=\"$country\"]/ancestor::Team";
      $result = $xml->xpath($query);
      foreach ($result as $node) {
        $this->sxml_append($returnXML, $node);
      }
    }
    return $returnXML->asXML();
  }

  function getSmallestTeamID() {
    $xml = simplexml_load_file("1_data.xml");
    $query = "//Team/@teamid[not(. > //Team/@teamid)]";
    $result = $xml->xpath($query);
    return $result[0];
  }

  function getCustomerByID($ID) {
    $xml = simplexml_load_file("2_data.xml");
    $returnXML = new SimpleXMLElement('<Customer></Customer>');    
    $query = "//Customer[@customerid = \"$ID\"]/Firstname | //Customer[@customerid = \"$ID\"]/Lastname";
    $result = $xml->xpath($query);
    foreach ($result as $node) {
      $this->sxml_append($returnXML, $node);
    }
    return json_encode($returnXML, JSON_PRETTY_PRINT);
  }

  function getPlanesByColor($colors) {
    $xml = simplexml_load_file("4_data.xml");
    $sxml = simplexml_load_string('<Planes></Planes>');

    foreach ($colors->color as $color) {
      $query = "//Color[.=\"$color\"]/ancestor::Plane";
      $result = $xml->xpath($query);
      foreach ($result as $node) {
        $this->sxml_append($sxml, $node);
      }
    }
    return $sxml->asXML();
  }

  function getPlanesByLivery($liveries) {
    $xml = simplexml_load_file("4_data.xml");
    $sxml = simplexml_load_string('<Planes></Planes>');

    foreach ($liveries->livery as $livery) {
      //$color = $colors->color[1];
      $query = "//Livery[.=\"$livery\"]/ancestor::Plane";
      $result = $xml->xpath($query);
      foreach ($result as $node) {
        $this->sxml_append($sxml, $node);
      }
    }
    return json_encode($sxml, JSON_PRETTY_PRINT);
  }

  function getProtocolByDate($date) {
    $xml = simplexml_load_file("2_data.xml");
    $query = "//Testdate[.=\"$date\"]/ancestor::Protocol";
    $result = $xml->xpath($query);
    $returnXML = new SimpleXMLElement('<Protocols></Protocols>');    
    foreach ($result as $node) {
      $this->sxml_append($returnXML, $node);
    }
    return $returnXML->asXML();
  }

  function getToiletsBetweenFlowrates($flowrates) {
    $minRate = $flowrates->minRate;
    $maxRate = $flowrates->maxRate;
    $xml = simplexml_load_file("3_data.xml");
    $query = "//Flowrate[(.>$minRate and .<$maxRate)]/ancestor::ToiletSpecs";
    $result = $xml->xpath($query);
    $returnXML = new SimpleXMLElement('<ToiletUnits></ToiletUnits>');    
    foreach ($result as $node) {
      $this->sxml_append($returnXML, $node);
    }
    return $returnXML->asXML();
  }
}
if ($_SERVER['REQUEST_METHOD'] == 'GET') {
  header('content-type: text/plain');
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  ini_set("soap.wsdl_cache_enabled", "0");
  $server = new SoapServer('airplanemanufacturing.wsdl');
  $server->setClass('Server');
  $server->handle();
  exit;
}

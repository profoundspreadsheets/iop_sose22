<?php
ini_set("soap.wsdl_cache_enabled", "0");
try {
  $client = new SoapClient('airplanemanufacturing.wsdl', array('trace' => 1));
  
  print("These services cover 8 xpath queries from ass3c.");
  print("<br />");
  
  print("getTeamsByEmployees(3) | 1_data.xml | R2, R7 | xpath11.xp");
  print("<br />");
  $result11 = simplexml_load_string($client->getTeamsByEmployees(3));
  $firstNode11 = $result11->xpath("//Team[1]");
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities($firstNode11[0]->asXML()), '</pre>';
  print("<br />");
  print("<br />");

  print("getTeamsByCountries(\$countries12)) | 1_data.xml | R1, R5.1, R7 | xpath12.xp");
  print("<br />");
  print("\$countries12 = (IS, IT)");
  print("<br />");
  $countries12 = array('IS', 'IT');
  $result12 = simplexml_load_string($client->getTeamsByCountry($countries12));
  $firstNode12 = $result12->xpath("//Team[1]");
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities($firstNode12[0]->asXML()), '</pre>';
  print("<br />");
  print("<br />");

  print("getSmallestTeamID() | 1_data.xml |  | xpath14.xp");
  print("<br />");
  $result14 = $client->getSmallestTeamID();
  print_r($result14);
  print("<br />");
  print("<br />");

  print("getCustomerByID(119) | 2_data.xml | R2, R6 | xpath23.xp");
  print("<br />");
  $result23 = $client->getCustomerByID(119);
  echo '<pre>', htmlentities($result23), '</pre>';
  print("<br />");
  print("<br />");

  print("getCustomersByZip(10000) | 3_data.xml | R2, R6 | xpath32.xp");
  print("<br />");
  $result32 = $client->getCustomersByZip(10000);
  $jsonResult32 = json_decode($result32);
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities(json_encode($jsonResult32->Customer[0], JSON_PRETTY_PRINT)), '</pre>';
  print("<br />");
  print("<br />");

  print("getStreetsByZip(10000) | 3_data.xml | R2, R6 | xpath31.xp");
  print("<br />");
  $result31 = $client->getStreetsByZip(10000);
  echo '<pre>', htmlentities($result31), '</pre>';
  print("<br />");
  print("<br />");

  print("getBarsOfPlane(RTM7433)) | 4_data.xml | R3, R6 | xpath41.xp");
  print("<br />");
  $result41 = $client->getBarsOfPlane('RTM7433');
  echo '<pre>', htmlentities($result41), '</pre>';
  print("<br />");
  print("<br />");

  print("getBarMinifridgeAndColor(\$requestArray42)) | 4_data.xml | R5.3 R7 | xpath42.xp");
  print("<br />");
  print("\$requestArray42 = (\$colors42, \$fridgesInterval42)");
  print("\n");
  print("\$colors42 = ('white', 'maroon') \n");
  print("\$fridgesInterval42 = (8, 10)");
  print("<br />");
  $colors42 = array('white', 'maroon');
  $fridgesInterval42 = array("minFridges" => 8, "maxFridges" => 10);
  $requestArray42 = array("colors" => $colors42, "fridgesInterval" => $fridgesInterval42);
  $result42 = simplexml_load_string($client->getBarMinifridgeAndColor($requestArray42));
  echo '<pre>', htmlentities($result42->asXML()), '</pre>';
  print("<br />");
  print("<br />");

  print("These services cover the remaining rules from ass5a.");
  print("<br />");

  print("getPlanesByColor(\$colors)) | 4_data.xml | R1 R5.1 R7 | ");
  print("<br />");
  print("\$colors = ('white', 'maroon')");
  print("<br />");
  $colors = array('white', 'maroon');
  $resultColors = simplexml_load_string($client->getPlanesByColor($colors));
  $firstNodeColors = $resultColors->xpath("//Plane[1]");
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities($firstNodeColors[0]->asXML()), '</pre>';
  print("<br />");
  print("<br />");

  print("getPlanesByLivery(\$liveries)) | 4_data.xml | R1 R5.1 R6 | ");
  print("<br />");
  print("\$liveries = ('eurowhite', 'jellybean')");
  print("<br />");
  $liveries = array('eurowhite', 'jellybean');
  $resultLivery = json_decode($client->getPlanesByLivery($liveries));
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities(json_encode($resultLivery->Plane[0], JSON_PRETTY_PRINT)), '</pre>';
  print("<br />");
  print("<br />");

  print("getProtocolByDate(\"2017-06-12\") | 2_data.xml | R4, R7 |");
  print("<br />");
  $resultDate = simplexml_load_string($client->getProtocolByDate("2017-06-12"));
  $firstNodeDate = $resultDate->xpath("//Protocol[1]");
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities($firstNodeDate[0]->asXML()), '</pre>';
  print("<br />");
  print("<br />");

  print("getToiletsBetweenFlowrates(\$flowrates) | 3_data.xml | R2, R5.2, R7 |");
  print("<br />");
  print("\$flowrates = (\"minRate\" => 2.0, \"maxRate\" => 2.5)");
  print("<br />");
  $flowrates = array("minRate" => 2.0, "maxRate" => 2.5);
  $resultFlowrates = simplexml_load_string($client->getToiletsBetweenFlowrates($flowrates));
  $firstNodeFlowrates = $resultFlowrates->xpath("//ToiletSpecs[1]");
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities($firstNodeFlowrates[0]->asXML()), '</pre>';
  print("<br />");
  print("<br />");

  print("getCustomerOfPlane('PLS5902')) | 3_data.xml | R3, R6 | ");
  print("<br />");
  $resultCustomerOfPlane = json_decode($client->getCustomerOfPlane("PLS5902"));
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities(json_encode($resultCustomerOfPlane->Customer[0], JSON_PRETTY_PRINT)), '</pre>';
  print("<br />");
  print("<br />");

  print("getTestdateOfProtocol('KPTDTWVNUZ')) | 2_data.xml | R3, R6 | ");
  print("<br />");
  $resultTestdateOfProtocol = json_decode($client->getTestdateOfProtocol("KPTDTWVNUZ"));
  print("first node:");
  print("<br />");
  echo '<pre>', htmlentities(json_encode($resultTestdateOfProtocol->Testdate[0], JSON_PRETTY_PRINT)), '</pre>';
  print("<br />");
  print("<br />");

} catch (SoapFault $e) {
  print_r($e);
}

<?php
ini_set("soap.wsdl_cache_enabled", "0");
$debug = true;
try {
  $client = new SoapClient('airplanemanufacturing.wsdl', array('trace' => 1));
  $colors = array('white', 'maroon');
  $fridgesInterval = array("minFridges" => 8, "maxFridges" => 10);
  $requestArray = array("colors" => $colors, "fridgesInterval" => $fridgesInterval);
  $result = $client->getBarMinifridgeAndColor($requestArray);

  header('content-type: text/plain');

  var_dump($result);

  print("\n");

  if ($debug) {
    $doc = new DOMDocument('1.0');
    $doc->formatOutput = true;
    $doc->loadXML($client->__getLastRequest());
    print $doc->saveXML();

    print("\n");

    $doc = new DOMDocument('1.0');
    $doc->formatOutput = true;
    $doc->loadXML($client->__getLastResponse());
    print $doc->saveXML();
  }
} catch (SoapFault $e) {
  print_r($e);
  print("<br / >");
  print_r($requestArray);
}

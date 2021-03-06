<?php
ini_set("soap.wsdl_cache_enabled", "0");
$debug = false;
try {
  $colors = array('maroon', 'white');
  $client = new SoapClient('airplanemanufacturing.wsdl', array('trace' => 1));
  $result = $client->getPlanesByColor($colors);

  header('content-type: text/plain');

  print_r($result);

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
  print_r($colors);
  print_r($e);
}

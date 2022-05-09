<?php
ini_set("soap.wsdl_cache_enabled", "0");
try {
  $client = new SoapClient('airplanemanufacturing.wsdl', array('trace' => 1));
  $flowrates = array("minRate" => 2.0, "maxRate" => 2.5);
  $result = $client->getToiletsBetweenFlowrates($flowrates);

  header('content-type: text/plain');

  print_r($result);

  print("\n");

  $doc = new DOMDocument('1.0');
  $doc->formatOutput = true;
  $doc->loadXML($client->__getLastRequest());
  print $doc->saveXML();

  print("\n");

  $doc = new DOMDocument('1.0');
  $doc->formatOutput = true;
  $doc->loadXML($client->__getLastResponse());
  print $doc->saveXML();
} catch (SoapFault $e) {
  print_r($flowrates);
  print_r("\n");
  print_r($e);
}


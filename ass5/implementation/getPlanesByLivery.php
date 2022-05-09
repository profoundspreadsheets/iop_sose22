<?php
ini_set("soap.wsdl_cache_enabled", "0");
$debug = false;
try {
  $liveries = array('eurowhite', 'jellybean');
  $client = new SoapClient('airplanemanufacturing.wsdl', array('trace' => 1));
  $result = $client->getPlanesByLivery($liveries);

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
  print_r($liveries);
  print_r($e);
}

<?php
ini_set("soap.wsdl_cache_enabled", "0");
$debug = false;
try {
  $client = new SoapClient('airplanemanufacturing.wsdl', array('trace' => 1));
  $dateString = "2017-06-12";
  $date = date("Y-m-d", strtotime($dateString));
  $result = $client->getProtocolByDate($date);

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
  print_r($dateString);
  print("\n");
  print_r(strtotime($dateString));
  print("\n");
  print_r($date);
  print("\n");
  print_r($e);
}

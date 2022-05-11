<?php
ini_set("soap.wsdl_cache_enabled", "0");
try {
  $client = new SoapClient('airplanemanufacturing.wsdl', array('trace' => 1));
  
  print("getCustomerByID");
  print("<br />");
  $result = $client->getCustomerByID(119);
  print_r($result);
  print("<br />");
  print("<br />");

  print("getStreetsByZip");
  print("<br />");
  $result = $client->getStreetsByZip(10000);
  print_r($result);
  print("<br />");
  print("<br />");

} catch (SoapFault $e) {
  print_r($e);
}

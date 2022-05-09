<?php

ini_set("soap.wsdl_cache_enabled", "0");
try {
  include_once 'getCustomerByID.php';
  include_once 'getPlanesByColor.php';
  include_once 'getPlanesByLivery.php';
  include_once 'getSmallestTeamID.php';
  include_once 'getTeamsByCountry.php';
  include_once 'getTeamsByEmployees.php';
  include_once 'getToiletsBetweenFlowrates.php';

  print("\n");
} catch (SoapFault $e) {
  print_r($e);
}

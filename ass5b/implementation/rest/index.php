<?php

use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';



$app = AppFactory::create();
$app->setBasePath("/~bartlp20/rest/index.php");
$app->addBodyParsingMiddleware();

$app->get('/', function (Request $request, Response $response, $args) {
  $response->getBody()->write("XMLs");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='http://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/1_data.xml'>1_data.xml</a><br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/2_data.xml'>2_data.xml</a><br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/3_data.xml'>3_data.xml</a><br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/4_data.xml'>4_data.xml</a><br>");
  return $response;
});

$app->get('', function (Request $request, Response $response, $args) {
  $response->getBody()->write("XMLs");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='http://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/1_data.xml'>1_data.xml</a><br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/2_data.xml'>2_data.xml</a><br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/3_data.xml'>3_data.xml</a><br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/4_data.xml'>4_data.xml</a><br>");
  return $response;
});


/**
 * GET METHODS
 */
$app->get('/teams/byemployees/{numEmployees}', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getTeamsByEmployees
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getTeamsByEmployees($args['numEmployees']));
  return $response;
});

$app->get('/teams/bycountries', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getSmallestTeamID
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $requestBody = $request->getParsedBody();
  $response->getBody()->write(getTeamsByCountries($requestBody));
  return $response;
});

$app->get('/teams/smallest', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getTeamsByCountries
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $smallestTeamID = getSmallestTeamID();
  $response->getBody()->write(strval($smallestTeamID));
  return $response;
});

$app->get('/customers/byzip/{zip}', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getCustomersByZip
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getCustomersByZip($args['zip']));
  return $response;
});

$app->get('/streets/byzip/{zip}', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getStreetsByZip
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getStreetsByZip($args['zip']));
  return $response;
});

$app->get('/bars/byminifridgesorcolor/', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getBarsMinifridgeAndColor
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $requestBody = $request->getParsedBody();
  $response->getBody()->write(getBarsMinifridgeAndColor($requestBody));
  return $response;
});

$app->get('/planes/bycolor/', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getPlanesByColor
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $requestBody = $request->getParsedBody();
  $response->getBody()->write(getPlanesByColor($requestBody));
  return $response;
});

$app->get('/planes/bylivery/', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getPlanesByLivery
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $requestBody = $request->getParsedBody();
  $response->getBody()->write(getPlanesByLivery($requestBody));
  return $response;
});

$app->get('/protocol/bydate/{date}', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getProtocolByDate
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getProtocolByDate($args['date']));
  return $response;
});




/**
 * POST METHODS
 */
$app->post('/planes/bars/postnewbar', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getBarsOfPlane
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $requestBody = $request->getParsedBody();
  $requestResult = postNewBar($requestBody);
  return $response;
});

/**
 * DELETE METHODS
 */
$app->delete('/customers/delete/{customerId}', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getCustomerByID
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $customerId = $args['customerId'];
  $requestResult = deleteCustomerById($customerId);
  if ($requestResult) {
    return $response->withStatus(204);
  } else {
    $response->getBody()->write("Could not delete customer with id: $customerId");
    return $response->withStatus(404);
  }
  return $response;
});

/**
 * PUT METHODS
 */
$app->put('/planes/update', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getCustomerOfPlane
   */
  $response = $response->withHeader('Content-Type', 'application/json');
  $requestBody = $request->getParsedBody();
  $requestResult = updateCustomerAddressByRegistration($requestBody);


  return $response->withStatus(200);


  // if ($requestResult) {
  //   $response->getBody()->write("requestBody");
  //   $response->getBody()->write($requestResult);
  //   return $response->withStatus(204); 
  //   // run another GET request to get new address
  // } else {
  //   return $response->withStatus(404);
  // }
  // return $response;
});

/**
 * PATCH METHODS
 */
$app->patch('/planes/bars/patchmeadrink', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getBarsOfPlane
   */
  $response = $response->withHeader('Content-Type', 'application/merge-patch+json');
  $requestBody = $request->getParsedBody();
  $requestResult = patchBeverage($requestBody);
  //$response->getBody()->write($requestBody['unitid']);
  if ($requestResult) {
    return $response->withStatus(200);
  } else {
    return $response->withStatus(404);
  }
});

$app->patch('/planes/toiletunits/betweenflowrate', function (Request $request, Response $response, $args) {
  /**
   * SOAP operation getToiletsBetweenFlowrates
   */
  $response = $response->withHeader('Content-Type', 'application/merge-patch+json');
  $requestBody = $request->getParsedBody();
  $requestResult = patchFlowrate($requestBody);
  if ($requestResult) {
    $response->getBody()->write($requestResult);
    return $response->withStatus(200);
  } else {
    return $response->withStatus(404);
  }
});

/**
 * GET METHODS HELPERS
 */
function getTeamsByEmployees($numEmployees) {
  $xml = simplexml_load_file("xmls/1_data.xml");
  $returnXML = new SimpleXMLElement('<Teams></Teams>');
  $query = "//Team[@employees <= $numEmployees]";
  $result = $xml->xpath($query);
  foreach ($result as $node) {
    sxml_append($returnXML, $node);
  }
  return json_encode($returnXML);
}

function getSmallestTeamID() {
  $xml = simplexml_load_file("xmls/1_data.xml");
  $query = "//Team/@teamid[not(. > //Team/@teamid)]";
  $result = $xml->xpath($query);
  return $result[0];
}


function getCustomersByZip($zip) {
  $xml = simplexml_load_file("xmls/3_data.xml");
  $query = "//Address[@zip < \"$zip\"]/ancestor::Customer";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<Customers></Customers>');
  foreach ($result as $node) {
    sxml_append($returnXML, $node);
  }
  return json_encode($returnXML);
}

function getStreetsByZip($zip) {
  $xml = simplexml_load_file("xmls/3_data.xml");
  $query = "//Address[@zip < \"$zip\"]/descendant::Street";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<Streets></Streets>');
  foreach ($result as $node) {
    sxml_append($returnXML, $node);
  }
  return json_encode($returnXML);
}

function getTeamsByCountries($countries) {
  $xml = simplexml_load_file("xmls/1_data.xml");
  $returnXML = new SimpleXMLElement('<Teams></Teams>');
  foreach ($countries['countries'] as $country) {
    $code = $country['country'];
    $query = "//ISO_Code[.=\"$code\"]/ancestor::Team";
    $result = $xml->xpath($query);
    foreach ($result as $node) {
      sxml_append($returnXML, $node);
    }
  }
  return json_encode($returnXML);
}

function getBarsMinifridgeAndColor($requestBody) {

  $colors = $requestBody['colors'];
  $minFridges = $requestBody['fridgesInterval']['minFridges'];
  $maxFridges = $requestBody['fridgesInterval']['maxFridges'];


  $xml = simplexml_load_file("xmls/4_data.xml");
  $returnXML = new SimpleXMLElement('<Registrations></Registrations>');
  foreach ($colors as $color) {
    // query is returning x amount of registrations if second test is satisfied
    // for x amount of color in colors
    $colorQuery = "//Color[.=\"$color\"]//ancestor::Plane | //Plane[descendant::Minifridges/Amount[.>$minFridges and .<$maxFridges]]";
    $result = $xml->xpath($colorQuery);
    foreach ($result as $node) {
      // convert attribute in node
      $newNode = new SimpleXMLElement('<Registration></Registration>');
      $newNode[0] = $node->attributes()->registration;
      sxml_append($returnXML, $newNode);
    }
  }
  return json_encode($returnXML);
}

function getPlanesByColor($requestBody) {
  $colors = $requestBody['colors'];
  $xml = simplexml_load_file("xmls/4_data.xml");
  $sxml = simplexml_load_string('<Planes></Planes>');
  foreach ($colors as $color) {
    $query = "//Color[.=\"$color\"]/ancestor::Plane";
    $result = $xml->xpath($query);
    foreach ($result as $node) {
      sxml_append($sxml, $node);
    }
  }
  return $sxml->asXML();
}

function getPlanesByLivery($requestBody) {
  $liveries = $requestBody['liveries'];
  $xml = simplexml_load_file("xmls/4_data.xml");
  $sxml = simplexml_load_string('<Planes></Planes>');
  foreach ($liveries as $livery) {
    $query = "//Livery[.=\"$livery\"]/ancestor::Plane";
    $result = $xml->xpath($query);
    foreach ($result as $node) {
      sxml_append($sxml, $node);
    }
  }
  return json_encode($sxml);
}

function getProtocolByDate($date) {
  $xml = simplexml_load_file("xmls/2_data.xml");
  $query = "//Testdate[.=\"$date\"]/ancestor::Protocol";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<Protocols></Protocols>');
  foreach ($result as $node) {
    sxml_append($returnXML, $node);
  }
  return $returnXML->asXML();
}

/**
 * DELETE METHODS HELPERS
 */
function deleteCustomerById($customerId) {
  $doc = new DOMDocument();
  $doc->load("xmls/2_data.xml");
  $xpath_selector = new DOMXPath($doc);
  $node_list = $xpath_selector->query("//Customer[@customerid = $customerId]");
  $node = $node_list->item(0);
  if ($node) {
    $node->parentNode->removeChild($node);
    file_put_contents("xmls/2_data.xml", $doc->saveXML());
    return true;
  } else {
    return false;
  }
}

/**
 * PUT METHODS HELPERS
 */
function updateCustomerAddressByRegistration($requestBody) {
  $registration = $requestBody['registration'];
  $newaddressbody = $requestBody['Address'];
  $zip = $newaddressbody['@attributes']['zip'];
  $city = $newaddressbody['@attributes']['city'];
  $street = $newaddressbody['Street'];
  $housenumber = $newaddressbody['Housenumber'];

  // get node and old data
  $doc = new DOMDocument();
  $doc->load("xmls/3_data.xml");
  $xpath_selector = new DOMXPath($doc);
  $node_list = $xpath_selector->query("//Plane[@registration = \"$registration\"]");
  $customer = $xpath_selector->query("//Plane[@registration = \"$registration\"]/Customer")->item(0);
  $oldAddress = $xpath_selector->query("//Plane[@registration = \"$registration\"]/Customer/Address")->item(0);
  $toilets = $xpath_selector->query("//Plane[@registration = \"$registration\"]/Toilets")->item(0);
  $node = $node_list->item(0);

  // new DOMElement is read only, rip 
  // set up new node and replace
  $plane = $doc->createElement("Plane");
  $plane->setAttribute("registration", $registration);
  $newAddress = $doc->createElement("Address");
  $newAddress->setAttribute("zip", $zip);
  $newAddress->setAttribute("city", $city);
  $streetElement = $doc->createElement("Street", $street);
  $housenumberElement = $doc->createElement("Housenumber", $housenumber);

  $newAddress->appendChild($streetElement);
  $newAddress->appendChild($housenumberElement);

  $customer->replaceChild($newAddress, $oldAddress);
  $plane->appendChild($customer);
  $plane->appendChild($toilets);

  $node->parentNode->replaceChild($plane, $node);

  file_put_contents("xmls/3_data.xml", $doc->saveXML());
  return true;
}

/**
 * POST METHODS HELPERS
 */
function postNewBar($requestBody) {
  $registration = $requestBody['registration'];
  $teamid = $requestBody['teamid'];
  $newBarData = $requestBody['Bar'];
  $amountMinifridges = $newBarData['Minifridges']['Amount'];
  $typeGlasses = $newBarData['Glasses']['Type'];
  $amountGlasses = $newBarData['Glasses']['Amount'];



  $doc = new DOMDocument();
  $doc->load("xmls/4_data.xml");
  $xpath_selector = new DOMXPath($doc);
  $planeNode = $xpath_selector->query("//Plane[@registration = \"$registration\"]")->item(0);

  $newBarNode = $doc->createElement("Bar");

  $uuid = getuuid();
  $newBarNode->setAttribute("unitid", $uuid);
  $newBarNode->setAttribute("teamid", $teamid);

  $fridgeNode = $doc->createElement("Minifridges");
  $fridgeNodeAmount = $doc->createElement("Amount", $amountMinifridges);

  $glassNode = $doc->createElement("Glasses");
  $glassNodeAmount = $doc->createElement("Amount", $amountGlasses);
  $glassNodeType = $doc->createElement("Type", $typeGlasses);

  $glassNode->appendChild($glassNodeType);
  $glassNode->appendChild($glassNodeAmount);

  $fridgeNode->appendChild($fridgeNodeAmount);

  $newBarNode->appendChild($fridgeNode);
  $newBarNode->appendChild($glassNode);

  $planeNode->appendChild($newBarNode);
  file_put_contents("xmls/4_data.xml", $doc->saveXML());

  return true;
}

/**
 * PATCH METHODS HELPERS
 */
function patchBeverage($requestBody) {
  // check for malformed body
  if (!isset($requestBody['unitid'])) {
    return false;
  }

  $unitid = $requestBody['unitid'];
  $beverages = $requestBody['Beverage'];

  $doc = new DOMDocument();
  $doc->load("xmls/4_data.xml");
  $xpath_selector = new DOMXPath($doc);
  $barNode = $xpath_selector->query("//Bar[@unitid = \"$unitid\"]")->item(0);
  //no node found
  if (!$barNode) {
    return false;
  }

  foreach ($beverages as $beverage) {
    $newBeverage = $doc->createElement("Beverage");
    $newBeverageDrink = $doc->createElement("Drink", $beverage['Drink']);
    $newBeverageCost = $doc->createElement("Cost", $beverage['Cost']);
    $newBeverage->appendChild($newBeverageDrink);
    $newBeverage->appendChild($newBeverageCost);

    $oldBeverages = $barNode->getElementsByTagName("Beverage");

    foreach ($oldBeverages as $oldBeverage) {
      // check if already exist, and replace if yes otherwise append 
      if ($oldBeverage->getElementsByTagName("Drink")->item(0)->textContent == $beverage['Drink']) {
        $oldBeverage->parentNode->replaceChild($newBeverage, $oldBeverage);
        break;
      } else {
        $oldBeverage->parentNode->appendChild($newBeverage);
      }
    }
  }
  file_put_contents("xmls/4_data.xml", $doc->saveXML());
  return true;
}

function patchFlowrate($requestBody) {
  // check for malformed body
  if (!isset($requestBody['flowrates'])) {
    return false;
  }

  $extraRegistration = $requestBody['registration'];
  $newFlowrate = $requestBody['newFlowrate'];
  $minRate = $requestBody['flowrates']['minRate'];
  $maxRate = $requestBody['flowrates']['maxRate'];

  $doc = new DOMDocument();
  $doc->load("xmls/3_data.xml");
  $query = "//Flowrate[(.>$minRate and .<$maxRate)]/ancestor::ToiletSpecs";
  $xpath_selector = new DOMXPath($doc);
  $result = $xpath_selector->query($query);
  $changedToiletUnits = new SimpleXMLElement("<Units></Units>");
  $extraRegistrationWasChanged = false;

  foreach ($result as $toilet) {

    // check if registration is in given toilets by interval
    $toilets = $toilet->parentNode;
    $plane = $toilets->parentNode;

    $changedRegistration = $plane->getAttribute('registration');
    if ($changedRegistration == $extraRegistration) {
      $extraRegistrationWasChanged = true;
    }

    $unitid = $toilet->getAttribute("unitid");
    $oldFlowrate = $toilet->getElementsByTagName("Flowrate")->item(0);
    $newFlowrateElement = new DOMElement("Flowrate", $newFlowrate);
    $oldFlowrate->parentNode->replaceChild($newFlowrateElement, $oldFlowrate);
    
    // return changes in body
    $changedToiletUnit = new SimpleXMLElement("<Unit></Unit>");
    $changedToiletUnit->addChild("operation", "modified");
    $changedToiletUnit->addChild("registration", $changedRegistration);
    $changedToiletUnit->addChild("unitid", $unitid);
    sxml_append($changedToiletUnits, $changedToiletUnit);
  }

  if (!$extraRegistrationWasChanged) {
    // extra specified registration was not changed, so add new toilet
    $planeNode = $xpath_selector->query("//Plane[@registration = \"$extraRegistration\"]")->item(0);
    $newToiletNode = $doc->createElement("ToiletSpecs");
    $uuid = getuuid();
    $newToiletNode->setAttribute("unitid", $uuid);
    $newCapacityNode = $doc->createElement("Capacity", "2000.00");
    $newFlowrateNode = $doc->createElement("Flowrate", $newFlowrate);
    $newToiletNode->appendChild($newCapacityNode);
    $newToiletNode->appendChild($newFlowrateNode);
    $planeNode->appendChild($newToiletNode);

    $changedToiletUnit = new SimpleXMLElement("<Unit></Unit>");
    $changedToiletUnit->addChild("operation", "created");
    $changedToiletUnit->addChild("registration", $extraRegistration);
    $changedToiletUnit->addChild("unitid", $uuid);
    sxml_append($changedToiletUnits, $changedToiletUnit);
  }

  file_put_contents("xmls/3_data.xml", $doc->saveXML());

  return json_encode($changedToiletUnits);
}

function sxml_append(SimpleXMLElement $to, SimpleXMLElement $from) {
  $toDom = dom_import_simplexml($to);
  $fromDom = dom_import_simplexml($from);
  $toDom->appendChild($toDom->ownerDocument->importNode($fromDom, true));
}

function getuuid() {
  // source: https://github.com/symfony/polyfill-uuid/blob/main/Uuid.php#L320
  $uuid = bin2hex(random_bytes(16));
  return sprintf(
    '%08s-%04s-4%03s-%04x-%012s',
    // 32 bits for "time_low"
    substr($uuid, 0, 8),
    // 16 bits for "time_mid"
    substr($uuid, 8, 4),
    // 16 bits for "time_hi_and_version",
    // four most significant bits holds version number 4
    substr($uuid, 13, 3),
    // 16 bits:
    // * 8 bits for "clk_seq_hi_res",
    // * 8 bits for "clk_seq_low",
    // two most significant bits holds zero and one for variant DCE1.1
    hexdec(substr($uuid, 16, 4)) & 0x3fff | 0x8000,
    // 48 bits for "node"
    substr($uuid, 20, 12)
  );
}



/**
 * HATEOAS Endpoints
 */

$app->get('/hateaos/customers', function (Request $request, Response $response, $args) {
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getHateaosCustomers());
  return $response;
});

$app->get('/hateaos/customers/{customerid}/info', function (Request $request, Response $response, $args) {
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getHateaosCustomersInfo($args['customerid']));
  return $response;
});

$app->get('/hateaos/customers/{customerid}/fullname', function (Request $request, Response $response, $args) {
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getHateaosCustomersFullname($args['customerid']));
  return $response;
});

$app->get('/hateaos/customers/{customerid}/planes', function (Request $request, Response $response, $args) {
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getHateaosCustomersPlanes($args['customerid']));
  return $response;
});


$app->get('/hateaos/customers/{customerid}/planes/{registration}/protocols', function (Request $request, Response $response, $args) {
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getHateaosCustomersProtocols($args['customerid'], $args['registration']));
  return $response;
});


function getHateaosCustomers() {
  $xml = simplexml_load_file("xmls/2_data.xml");
  $query = "//Customer";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<HateaosInfo></HateaosInfo>');
  $returnXML->addChild('Customer Info Endpoints', "/hateaos/customers/{customerid}/info");
  foreach ($result as $node) {
    $newNode = new SimpleXMLElement('<Customers></Customers>');
    $newNode[0] = $node->attributes()->customerid;
    sxml_append($returnXML, $newNode);
  }
  return json_encode($returnXML, JSON_UNESCAPED_SLASHES);
}


function getHateaosCustomersInfo($customerid) {
  $xml = simplexml_load_file("xmls/2_data.xml");
  $query = "//Customer[@customerid = \"$customerid\"]";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<HateaosInfo></HateaosInfo>');
  $customerinfo = new SimpleXMLElement('<customerinfo></customerinfo>');
  $node = $result[0];
  $newNode = new SimpleXMLElement('<customerid></customerid>');
  $newNode[0] = $node->attributes()->customerid;
  sxml_append($customerinfo, $newNode);
  $linksnode = new SimpleXMLElement('<links></links>');
  $linksnode->addChild('fullname', "/hateaos/customers/$customerid/fullname");
  $linksnode->addChild('planes', "/hateaos/customers/$customerid/planes");
  sxml_append($customerinfo, $linksnode);
  sxml_append($returnXML, $customerinfo);
  return json_encode($returnXML, JSON_UNESCAPED_SLASHES);
}

function getHateaosCustomersFullname($customerid) {
  $xml = simplexml_load_file("xmls/2_data.xml");
  $query = "//Customer[@customerid = \"$customerid\"]/Firstname | //Customer[@customerid = \"$customerid\"]/Lastname";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<HateaosInfo></HateaosInfo>');
  $newNode = new SimpleXMLElement('<customerid></customerid>');
  $newNode[0] = $customerid;
  sxml_append($returnXML, $newNode);
  $firstname = $result[0];
  $lastname = $result[1];
  $namesnode = new SimpleXMLElement('<fullname></fullname>');
  $namesnode->addChild('firstname', "$firstname");
  $namesnode->addChild('lastname', "$lastname");
  sxml_append($returnXML, $namesnode);
  return json_encode($returnXML, JSON_UNESCAPED_SLASHES);
}

function getHateaosCustomersPlanes($customerid) {
  $xml = simplexml_load_file("xmls/2_data.xml");
  $query = "//Customer[@customerid = \"$customerid\"]/Planes/Plane";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<HateaosInfo></HateaosInfo>');
  $returnXML->addChild("customerid", $customerid);
  foreach ($result as $plane) {
    $registration = $plane->attributes()->registration;
    $planeNode = new SimpleXMLElement('<plane></plane>');
    $planeNode->addAttribute("registration", $registration);
    $protocols = $plane->xpath("//Plane[@registration = \"$registration\"]/Protocols/Protocol");
    $linksNode = new SimpleXMLElement('<links></links>');
    if ($protocols) {
      // only add link if plane actually has protocols
      $linksNode->addChild("protocols", "/hateaos/customers/$customerid/planes/$registration/protocols");
    }
    sxml_append($planeNode, $linksNode);
    sxml_append($returnXML, $planeNode);
  }


  return json_encode($returnXML, JSON_UNESCAPED_SLASHES);
}

function getHateaosCustomersProtocols($customerid, $registration) {
  $xml = simplexml_load_file("xmls/2_data.xml");
  $query = "//Customer[@customerid = \"$customerid\"]/Planes/Plane[@registration = \"$registration\"]/Protocols/Protocol";
  $result = $xml->xpath($query);
  $returnXML = new SimpleXMLElement('<HateaosInfo></HateaosInfo>');
  $returnXML->addChild("customerid", $customerid);
  $returnXML->addChild("registration", $registration);
  foreach ($result as $protocol) {
    sxml_append($returnXML, $protocol);
  }
  return json_encode($returnXML, JSON_UNESCAPED_SLASHES);
}




$app->run();

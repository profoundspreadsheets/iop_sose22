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
$app->get('/teams/{numEmployees}', function (Request $request, Response $response, $args) {
  $response = $response->withHeader('Content-Type', 'application/json');
  $response->getBody()->write(getTeamsByEmployees($args['numEmployees']));
  return $response;
});

/**
 * DELETE METHODS
 * delete customer with ID
 */
$app->delete('/customers/delete/{customerId}', function (Request $request, Response $response, $args) {
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
 * update a customers address of plane with registration x
 */
$app->put('/planes/update', function (Request $request, Response $response, $args) {
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

function sxml_append(SimpleXMLElement $to, SimpleXMLElement $from) {
  $toDom = dom_import_simplexml($to);
  $fromDom = dom_import_simplexml($from);
  $toDom->appendChild($toDom->ownerDocument->importNode($fromDom, true));
}
















$app->run();

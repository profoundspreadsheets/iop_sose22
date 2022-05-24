<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';



$app = AppFactory::create();
$app->setBasePath("/~bartlp20/rest/index.php");
$app -> addErrorMiddleware(true,true,true);
$app->addBodyParsingMiddleware();


$app->get('', function (Request $request, Response $response, $args) {
  $response->getBody()->write("Hello world!");
  $response->getBody()->write("Zrrdz");
  $response->getBody()->write("<a href='http://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/1_data.xml'>1_data.xml</a>");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/2_data.xml'>2_data.xml</a>");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/3_data.xml'>3_data.xml</a>");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/4_data.xml'>4_data.xml</a>");
  $response->getBody()->write("<br>");
  return $response;
});

$app->get('/', function (Request $request, Response $response, $args) {
  $response->getBody()->write("Hello world!");
  $response->getBody()->write("Zrrdz");
  $response->getBody()->write("<a href='http://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/1_data.xml'>1_data.xml</a>");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/2_data.xml'>2_data.xml</a>");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/3_data.xml'>3_data.xml</a>");
  $response->getBody()->write("<br>");
  $response->getBody()->write("<a href='https://wwwlab.cs.univie.ac.at/~bartlp20/rest/xmls/4_data.xml'>4_data.xml</a>");
  $response->getBody()->write("<br>");
  return $response;
});


$app->run();



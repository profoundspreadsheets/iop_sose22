# Task Description

Your task is to create SOAP services (in any programming language of your choice) that implement some of the functionality from your XPATH queries (the ones you created in assignment 3c). You have to implement at least 8 of your XPATH queries as a function in your SOAP service.

Your SOAP operations have to fulfill the following requirements:
  - R1: at least 3 SOAP operations have to use arrays as input parameter
  - R2: at least 3 SOAP operations have to use floats or integers as input parameter
  - R3: at least 3 SOAP operations have to use strings as input parameter
  - R4: at least 1 SOAP operation has to use a date as input parameter
  - R5: at least 2 SOAP operations have to use complex data structures as input parameters which have to include:
    * R5.1: at least one array (of strings, integers, floats, ...)
    * R5.2: at least one hash/associative array/dictionary (of strings, integers, floats, ...)
    * R5.3: at least one array of objects which contains at least two elements (of type string, integer, float, ...)
  - R6: at least 3 SOAP operations need to return JSON
  - R7: at least 3 SOAP operations need to return XML

In addition implement one SOAP client in PHP that executes your SOAP services (server) and outputs their responses as a HTML page.

Examples for SOAP client and server implementations in php as well as for the WSDL file can be found here (and an example WSDL with a more complicated schema here) - more information about WSDL can be found in the standard.

Also read the article about different WSDL styles available here.

# Additional Requirements

    Requirements of earlier assignments still apply.
    If you require a dedicated port for your service, reserve a (new) port in the Forum (Port Reservation).
    IMPORTANT: Your services must run on almighty.cs/abgabe.cs server. Make sure that your service is running until grading is completed.
    See the access guide for almighty.cs and abgabe.cs.

# Submission

When: 12.05.2022 23:59
Where: Moodle
What: 3 zip files and 1 pdf file
Feedback: Via Moodle and discussion in class.

    xmls.zip: Contains your 4 XMLs (named "X_data.xml") as submitted for assignment 3c.
    queries.zip: Contains 16 XPath files labelled as xpathYZ.xp as submitted for assignment 3c.
    implementation.zip: Contains the implementation of your SOAP service.
    - Label your SOAP Client as soap_client.php.
    - Provide a bash script 'run.sh' that executes your service (not as a background process).
    implementation.pdf: As first line should contain the address of the WSDL (which points to the SOAP service you created). Furthermore, for each of the created SOAP functions, document:
      - its purpose
      - its return data (shorten it to 10 lines if it returns more than that)
      - a table documenting which of the requirements are fulfilled by this function


# Assessment Criteria
Points will be deducted for
* errors,
* SOAP functions that are not executable,
* missing documentation,
* failing to fulfill the requirements,
* malformed submissions and file naming.
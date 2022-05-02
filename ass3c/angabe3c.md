# Task Description

In this task you should get familiarised with XPath for extracting information from XML. For this create 4 XPath 1.0 compliant (i.e. without extensions) queries for each of your extracted XML. In total you should have sixteen queries. 
 
Rules: 

    C1: At least 6 queries must consider information that is stored in attributes. 
    C2: At least 5 queries must return nodes while considering information from their descendants.
    C3: At least 5 queries must return nodes while considering information from their ancestors.
    C4: At least 2 queries must return nodes while considering information from their descendants and ancestors. (Update: Counts towards C2 and C3 )
    C5: At least 5 queries must use aggregate functions. 
    C6: At least 2 queries must union result sets.
    C7: At least 1 query must find the maximum or minimum of something (min() or max() are not permitted). 


Additional Requirements

    Requirements of Assignment 1, 2, and 3a-b still apply!
    Your queries must be runnable! Test them with e.g. xpath or xmllint, both available under Linux:

    xpath -e '//foo[@bar = "foo-bar"]' data.xml
    xmllint -xpath '//foo[@bar = "foo-bar"]' data.xml

# Submission

When: 07.04.2022 23:59
Where: Moodle
What: 2 .pdf, 4 .zip, 1 .db
Feedback: Via Moodle and discussion in class.

    xpath.pdf: Create a wide format PDF of 4 pages. Each page must document your XPaths for one XML. See example bellow for the format expected. Use a table.

    Format for each query:

    | C1 | C2 | ... | Cn |         <- Columns of Rules
      X               X            <- Rules you fulfilled
    Get all bar nodes with name foobar  <- One sentence what the XPath does
    /foo/bar[@name="foobar"]       <- XPath Expression

    Add a 5th page that summarises how many times a rule has been applied.
    | C1 | C2 | ... | Cn |         <- Columns of Rules
                                   <-  Number of times the rule has been used overall.
     
    xpaths.zip: Must include 16 XPath files labelled as xpathYZ.xp where the capital letter Y denotes the number of the XML (X in X_data.xml) and Z a number from 1 to 4. The files should only contain the XPath expression.

    model.pdf: (Updated) documentation from Assignment 3b including clearly highlighted updates if something had to be changed to meet requirements of former tasks.
    schemas.zip: Must include 4 RNG schemas named X_schema.rng where X is a number from 1-4 (e.g. 1_schema.rng). Your files must validate the XML files in the xmls.zip using xmllint - 1_schema.rng must validate 1_data.xml, and so on!
    xmls.zip: Must include 4 files, each with the SQL query result of well-formed XMLs labelled as X_data.xml where X is a number from 1-4 (e.g. 1_data.xml). Your files must match the RNG files in the schemas.zip using xmllint - 1_schema.xml must validate 1_data.xml, and so on!
    queries.zip: Must include 4 raw SQL and 4 SQL queries with XML transformations labelled as X_raw.sql and X_xml.sql respectively where X is a number from 1-4 (e.g. 1_raw.sql, 1_xml.sql). Your files must be executable, i.e. use valid syntax if adding comments!
    data.db: From Assignment 2 (3a-b)

Assessment Criteria
Points will be deducted for
* errors,
* not executable XPath expressions,
* missing documentation,
* failing to fulfil the requirements,
* malformed submissions and file naming.
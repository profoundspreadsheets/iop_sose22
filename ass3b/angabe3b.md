# Task Description

Your task is to create 4 RELAX NG schemas (1 for each of your XMLs from assignment 3a) that match your XML files.

Your queries must fulfil the following requirements:

    Your schemas have to be different from each other.
    Each schema must contain grammar and start
    Each schema must contain at least 4 <define> elements
    Use at least the following concepts (for examples visit this website and search for the concept) for each schema:
    - zeroOrMore or oneOrMore
    - interleave
    - choice (for values)
    - choice (for elements or attributes)
    - optional
    - list

How we would approach this task:

    Start with one of your XMLs and take just the outermost element.
    Write a schema that you think matches the XML.
    Validate your schema using e.g., xmllint (in the command line in Linux this could look like this: xmllint --relaxng [RNG] [XML]).
    Add the next level of your XML file and repeat the steps described above.
    If you reach the last level, validate the whole XML file with your RNG schema.
    When you have completed all the RNGs, check if you fullfill all the requirements.


Additional Requirements

    Requirements form Assignment 1, 2, and 3a still apply!

    Your RNGs must validate the corresponding XMLs using the xmllint tool as described above.
    Don't 'overuse' the 'optional' element to ignore larger parts of your xml.

# Submission

When: 31.03.2021 - 23:59
Where: Moodle
What: 1 .pdf, 3 .zip, 1 .db
Feedback: Via Moodle and discussion in class.

    model.pdf: (Updated) documentation from Assignment 3a including clearly highlighted updates if something had to be changed to meet requirements of former tasks.
    schemas.zip: Must include 4 RNG schemas named X_schema.rng where X is a number from 1-4 (e.g. 1_schema.rng). Your files must validate the XML files in the xmls.zip using xmllint - 1_schema.rng must validate 1_data.xml, and so on!
    xmls.zip: Must include 4 files, each with the SQL query result of well-formed XMLs labelled as X_data.xml where X is a number from 1-4 (e.g. 1_data.xml). Your files must match the RNG files in the schemas.zip using xmllint - 1_schema.xml must validate 1_data.xml, and so on!
    queries.zip: Must include 4 raw SQL and 4 SQL queries with XML transformations labelled as X_raw.sql and X_xml.sql respectively where X is a number from 1-4 (e.g. 1_raw.sql, 1_xml.sql). Your files must be executable, i.e. use valid syntax if adding comments!
    data.db: From Assignment 2

Assessment Criteria
Points will be deducted for
* errors,
* schemas that cannot be used for validating the XMLs,
* missing documentation,
* failing to fulfil the requirements,
* malformed submissions and file naming.
# Task Description

Your task is to create 4 SQL queries that produce well-formed XMLs from your database. Use the XML and JSON functions provided by PostgresSQL.


Your queries must fulfil following requirements:

    Each raw SQL query (i.e. without the XML transformation) must yield at least 29 rows/tuples.
    Each raw SQL query must return at least 7 columns
    Each query must involve at least 3 tables (use joins!)

    No query is allowed to use the same 3 tables (combination, e.g. ABC is in use ->> ABD EBC ok, ABC ACB CAB ... not ok)
    Two queries have to use the XML columns
    Two queries have to use the JSON columns
    Use xmlelement, xmlagg and xmlforest (all three mandatory for each query)
    Use -> and ->> to extract json but also elementary values from your JSON columns (both are mandatory).
    Each XML result must have a depth of at least 5 levels of elements (including the root element) and at least 3 different attributes.


How we would approach this task:

    First write raw SQL queries and try to fulfil applicable requirements.
    Get familiar with the required XML and JSON functions for your queries.
    Understand what aggregation means in the context of SQL.
    Sketch a tree (considering the relational dependencies) for the desired structure of your XML results.
    Convert your raw SQL queries (inside-out) to XML SQL queries and fulfil remaining requirements.


Additional Requirements

    Requirements form Assignment 1 and 2 still apply!

    Database must be in 3rd Normal Form + requirements from Assignement 1 apply. If your model does not fulfil the requirements update your model.
    Export your database using the CLI tool psql and the following command
    pg_dump -Fc <db-name> > dump_<stundent_id>.db
    Your database dump must be importable in PostgreSQL 13 running on Fedora 35 using pg_restore.

# Submission

When: 24.03.2021 - 23:59
Where: Moodle
What: 1 .pdf, 2 .zip, 1 .db
Feedback: Via Moodle and discussion in class.

    model.pdf: (Updated) documentation from Assignment 2. Introduce a new Chapter (5)? That documents the raw query and its output of the first 10 rows and the queries including the XML transformations + first 15-30 lines of the XML output (XML example should include the full example of a reoccurring pattern). For each query highlight the elements which fufil the requirements.

    How to structure Chapter 5:

      raw SQL 1
      raw output SQL 1
      xml SQL 1
      xml output SQL 1
      ... repeat for 2-4


    queries.zip: Must include 4 raw SQL and 4 SQL queries with XML transformations labelled as X_raw.sql and X_xml.sql respectively where X is a number from 1-4 (e.g. 1_raw.sql, 1_xml.sql). Your files must be executable, i.e. use valid syntax if adding comments!
    xmls.zip: Must include 4 files, each with the SQL query result of well-formed XMLs labelled as X_data.xml where X is a number from 1-4 (e.g. 1_data.xml).
    data.db: From Assignment 2

Assessment Criteria
Points will be deducted for
* errors,
* not runnable queries,
* missing documentation,
* failing to fulfil the requirements,
* malformed submissions and file naming.
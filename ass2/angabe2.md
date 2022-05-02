# Task Description

Implement your database schema from Assignment 1 in PostgreSQL 13 and implement a data generator that fills each table with at least 777 rows of data.

The data should respect primary and foreign key constraints, i.e. the data rows should have relations. You may use external data sources (e.g. list of names, objects, ...) which your data generator may use to create input for your database.


Include the following data types in your tables (see available Data Types):

* at least 4 attributes of type integer (any integer)
* at least 4 attributes of type varchar
* at least 2 attributes of type timestamp (or date or time)
* at least 4 attributes of type float

* at least 2 attributes of type xml
* at least 2 attributes of type json (not jsonb)

The XML in the xml columns has to contain at least 3 levels of elements (including root element) and at least 2 different attributes. E.g.:
```xml
<address> <-- level 1-->
    <name> <-- level 2-->
        <given_name>Chuck</given_name>
        <family_name>Norris</family_name>
    </name>
    <address zip="1190" country="AT">
        <street> <-- level 3-->
        <name>Waehringerstrasse</name>  <-- level 4-->
        <number type="main">29</number>
        <number type="internal">4.49</number>
        </street>
        <city>Vienna</city>
    </address>
</address>
```

The JSON columns must also have a depth of at least 3 levels
```json
{
  "address": {  --> level 1
    "resident": {  --> level 2
      "given_name": "Chuck",  --> level 3
      "family_name": "Norris"
    },
    "zip": 1190,
    "street_name": "Waehringerstrasse",
    "no_main": 29,
    "no_internal": 4.49
  }
}
```

# How to install Postgres?

See the documentation here.

## On Fedora 35:
sudo -s
### DB Setup
dnf install postgresql postgresql-server
postgresql-setup initdb
systemctl start postgresql

### DB and User Creation
su - postgres
createuser <username> -P # <username> of your linux account - saves you from configuring special access policies in the pg_hba.conf
createdb <db-name> --owner=<username> # <db-name> can be any arbitrary database name.
exit # postgres
exit # root

### Postgres -CLI
psql -d <db-name> -U <username> # interactive console


Additional Requirements

    Database must be in 3rd Normal Form + requirements from Assignement 1 apply. If your model does not fulfil the requirements update your model.
    Export your database using the CLI tool psql and the following command
    pg_dump -Fc <db-name> > dump_<stundent_id>.db
    Your database dump must be importable in PostgreSQL 13 running on Fedora 35 using pg_restore.

# Submission

When: 20.03.2021 - 23:59
Where: Moodle
What: 1 PDF, 1 Code-ZIP, 1 Database Dump as .db

Feedback: Via Moodle and discussion in class.

    PDF: Extend your documentation from Assignment 1 with a Chapter 4 that shows screenshots of the first 15 tuples of each table.  
    If applicable update the your documentation with a revised data model.
    Code-ZIP: Should include the source code that creates the database schema in PostgresSQL and fills the database tables with data.
    Database Dump: The database dump exported with the psql tool as described above.

Assessment Criteria
Points will be deducted for
* errors,
* missing documentation,
* failing to fulfil the requirements,
* malformed submissions and file naming.
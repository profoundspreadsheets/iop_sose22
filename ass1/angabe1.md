# Task Description

Create one data model as an Entity-Relationship Diagram (use the Chen notation - not the MC notation!) and as an UML Class Diagram (don't use min-max notation) for your scenario (see assigned scenario below). Both diagrams should represent an identical data model. 


Each model must include at least:  

    at least 7 entities with relations in total 
    at least 2 strong entities 
    at least 2 weak entities 
    at least 6 attributes per entity 
    correct labels and cardinalities for each relation 
    correct primary keys and foreign keys 


Finally convert your data model into a Relational Database Schema (generic notation - see example). The database schema must be in 3rd normal form. The following is an example for a relational database schema that represents the relation between buildings and their rooms:

Building(BuildingName, Address)
PK: BuildingName

Room(BuildingName, RoomNo)
PK: BuildingName, RoomNo
FK: BuildingName ◊ Building


If something is unclear, use your imagination to solve the problem. Some ideas for entities: materials, locations (rooms, buildings), addresses, outputs, items, persons, jobs, … 

# Submission

When: 13.03.2021 - 23:59
Where: Moodle
What: 1 PDF
Feedback: Via Moodle and discussion in class.


The PDF should be in the wide format and structured as follows:

    Chapter I (First Page) - 'Data Model'
    One high resolution image of your ER diagram on the lhs of the first page and one high resolution image of your Class diagram on the rhs of the first page.

    Chapter II - 'Relational Database Schema' 
    Describes your database schema, i.e. your entities and relations in the format described under the task description. Futhermore document
        max 1-2 sentences about the meaning of each entity, 
        max 1-2 sentences how you choose the primary keys,
        max 1-2 sentences about each relation and its cardinalities.

    Chapter III 'Visualisation of the Database Schema'
    For each entity and relation from Chapter II provide 5 example tuples (rows) for each entity ( similar to how you would expect them in a relation database, including the primary and foreign keys). 

Chapter II and III may use any number of pages required. You can use our template for the submission.

Assessment Criteria
Points will be deducted for
* errors,
* missing documentation,
* failing to fulfil the requirements,
* malformed submissions and file naming. 
CREATE TABLE COUNTRY(
    ISO_Code CHAR(2) PRIMARY KEY,
    CountryName VARCHAR(50),
    Sanctioned BOOLEAN,
    Currency CHAR(3),
    Tariff FLOAT,
    Billionaires INTEGER
);

CREATE TABLE CUSTOMER(
    CustomerId SERIAL PRIMARY KEY,
    Firstname VARCHAR(50),
    Lastname VARCHAR(50),
    Birthday DATE,
    Street VARCHAR(50),
    Housenumber INTEGER,
    Zip INTEGER,
    City VARCHAR(50)
);

CREATE TABLE PLANE(
    Registration VARCHAR(10) PRIMARY KEY,
    CustomerId INTEGER,
    PlaneName VARCHAR(50),
    Color VARCHAR(50),
    Livery VARCHAR(50),
    Wingtips BOOLEAN,
    NumWindows INTEGER,
    Seats XML,
    FOREIGN KEY (CustomerId) REFERENCES CUSTOMER (CustomerId)
);

CREATE TABLE MANUFACTURINGTEAM(
    TeamId SERIAL PRIMARY KEY,
    ISO_Code CHAR(2),
    Employees INTEGER,
    HourlyRate FLOAT,
    Street VARCHAR(50),
    Housenumber INTEGER,
    Zip INTEGER,
    FOREIGN KEY (ISO_Code) REFERENCES COUNTRY (ISO_Code)
);

CREATE TABLE TOILETUNIT(
    UnitId VARCHAR(100) PRIMARY KEY,
    Registration VARCHAR(10),
    TeamId INTEGER,
    Cost FLOAT,
    ManufacturingTime TIME,
    Material VARCHAR(50),
    UnitVolume FLOAT,
    UnitWeight FLOAT,
    ToiletSpecs JSON,
    FOREIGN KEY (Registration) REFERENCES PLANE (Registration),
    FOREIGN KEY (TeamId) REFERENCES MANUFACTURINGTEAM (TeamId)
);

CREATE TABLE BARUNIT(
    UnitId VARCHAR(100) PRIMARY KEY,
    Registration VARCHAR(10),
    TeamId INTEGER,
    Cost FLOAT,
    ManufacturingTime TIME,
    Material VARCHAR(50),
    UnitVolume FLOAT,
    UnitWeight FLOAT,
    Features JSON,
    FOREIGN KEY (Registration) REFERENCES PLANE (Registration),
    FOREIGN KEY (TeamId) REFERENCES MANUFACTURINGTEAM (TeamId)
);

CREATE TABLE BEVERAGE(
    UnitId VARCHAR(100),
    BottleId VARCHAR(10),
    BeverageName VARCHAR(100),
    BeveragePercentage FLOAT,
    BeverageType VARCHAR(50),
    Cost FLOAT,
    Size FLOAT,
    PRIMARY KEY(UnitId, BottleId),
    FOREIGN KEY (UnitId) REFERENCES BARUNIT (UnitId) ON DELETE CASCADE
);

CREATE TABLE TESTPROTOCOL(
    Registration VARCHAR(10),
    ProtocolId VARCHAR(10),
    TestDate DATE,
    TestRoute VARCHAR(50),
    Airport VARCHAR(3),
    Pilot VARCHAR(50),
    Results XML,
    PRIMARY KEY(Registration, ProtocolId),
    FOREIGN KEY (Registration) REFERENCES PLANE (Registration) ON DELETE CASCADE
);

create or replace function 
count_rows(schema text, tablename text) returns integer
as
$body$
declare
  result integer;
  query varchar;
begin
  query := 'SELECT count(1) FROM ' || schema || '.' || tablename;
  execute query into result;
  return result;
end;
$body$
language plpgsql;

create or replace view rows_all_tables as
select 
  table_schema,
  table_name, 
  count_rows(table_schema, table_name)
from information_schema.tables
where 
  table_schema not in ('pg_catalog', 'information_schema') 
  and table_type='BASE TABLE'
order by 3 desc;
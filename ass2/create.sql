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
    Seats INTEGER,
    NumWindows INTEGER,
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
    Capacity FLOAT,
    Flowrate FLOAT,
    Bidet BOOLEAN,
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
    Minifridges INTEGER,
    FOREIGN KEY (Registration) REFERENCES PLANE (Registration),
    FOREIGN KEY (TeamId) REFERENCES MANUFACTURINGTEAM (TeamId)
);

CREATE TABLE BEVERAGE(
    UnitId VARCHAR(100),
    BottleId VARCHAR(10),
    BeverageName VARCHAR(10),
    BeveragePercentage FLOAT,
    BeverageType VARCHAR(10),
    Cost FLOAT,
    Size FLOAT,
    PRIMARY KEY(UnitId, BottleId),
    FOREIGN KEY (UnitId) REFERENCES BARUNIT (UnitId)
);

CREATE TABLE TESTPROTOCOL(
    Registration VARCHAR(10),
    ProtocolId VARCHAR(10),
    TestDate DATE,
    TestRoute VARCHAR(10),
    Test VARCHAR(10),
    Airport VARCHAR(10),
    Pilot VARCHAR(50),
    PRIMARY KEY(Registration, ProtocolId),
    FOREIGN KEY (Registration) REFERENCES PLANE (Registration)
);
from datetime import datetime
import json
from random import choice
from randomutil import RandomUtil
import psycopg2


class DatabaseFiller:
    def __init__(self):
        self.randomutil = RandomUtil()
        self.conn = None
        self.connect()

    def generateCountries(self):
        countries = self.randomutil.countries
        stmt = 'INSERT INTO country (iso_code, countryname, sanctioned, currency, tariff, billionaires) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(
                "XX", "Fallbackistan", False, "XXX", 50000000, 1
            )
        self.cursor.execute(stmt)
        for i in countries:
            isoCode = i[1]
            countryName = i[0]
            sanctioned = self.randomutil.getRandomBoolean(0.05)
            currency = i[3]
            tariff = self.randomutil.getRandomInteger(100000, 999999)
            billionaires = self.randomutil.getRandomInteger(1, 50)
            stmt = 'INSERT INTO country (iso_code, countryname, sanctioned, currency, tariff, billionaires) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(
                isoCode, countryName, sanctioned, currency, tariff, billionaires
            )
            self.cursor.execute(stmt)
        self.conn.commit()
            
    def generateCustomers(self, amount):
        for i in range(amount):
            firstname = self.randomutil.getRandomFirstname()
            lastname = self.randomutil.getRandomLastname()
            birthday = self.randomutil.getRandomDate(datetime(1940,1,1), datetime(2000,1,1))
            address = self.randomutil.getRandomAddress()
            stmt = 'INSERT INTO customer (firstname, lastname, birthday, street, housenumber, zip, city) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}, {}, \'{}\');'.format(
                firstname, lastname, birthday, address[0], address[1], address[2], address[3]
            )
            self.cursor.execute(stmt)
        self.conn.commit()

    def generateManufacturingTeams(self, amount):
        for i in range(amount):
            employees = self.randomutil.getRandomInteger(3, 20)
            hourlyRate = self.randomutil.getRandomFloat(50, 250)
            address = self.randomutil.getRandomAddress()
            stmt = 'INSERT INTO manufacturingteam (iso_code, employees, hourlyrate, street, housenumber, zip) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}, {});'.format(
                address[5], employees, hourlyRate, address[0], address[1], address[2]
            )
            self.cursor.execute(stmt)
        self.conn.commit()

    def generatePlanes(self, amount):
        self.cursor.execute("SELECT customerid FROM customer;")
        customers = self.cursor.fetchall()
        for i in range(amount):
            customer  = choice(customers)[0]
            registration = self.randomutil.createRandomString(3) + self.randomutil.createRandomNumberString(4)
            planename = self.randomutil.createRandomString(20)
            color = self.randomutil.getRandomColor()
            livery = self.randomutil.getRandomLivery()
            windows = self.randomutil.getRandomInteger(10, 120)

            seatseco = self.randomutil.getRandomInteger(10, 80)
            seatsbus = self.randomutil.getRandomInteger(8, 30)
            seatsfirst = self.randomutil.getRandomInteger(2, 8)

            seats = '<seats><compartment><eco><amount>{}</amount><cover>fabric</cover></eco><business><amount>{}</amount><cover>leather</cover></business><first><amount>{}</amount><cover>leather</cover></first></compartment><brand>Recaro</brand></seats>'.format(seatseco, seatsbus, seatsfirst)

            stmt = 'INSERT INTO plane (registration, customerid, planename, color, livery, numwindows, seats) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(
                registration, customer, planename, color, livery, windows, seats
            )
            self.cursor.execute(stmt)
        self.conn.commit()

    def generateToiletUnits(self, amount):
        self.cursor.execute("SELECT registration FROM plane;")
        planes = self.cursor.fetchall()

        self.cursor.execute("SELECT teamid FROM manufacturingteam;")
        teams = self.cursor.fetchall()

        for i in range(amount):
            unitid = self.randomutil.createUUID()
            plane  = choice(planes)[0]
            team = choice(teams)[0]
            cost = self.randomutil.getRandomFloat(20000, 150000)
            manufacturingtime = self.randomutil.getRandomTime()
            material = self.randomutil.getRandomMaterial()
            volume = self.randomutil.getRandomFloat(3, 15)
            weight = self.randomutil.getRandomFloat(100, 500)
            capacity = self.randomutil.getRandomFloat(5, 20)
            flowrate = self.randomutil.getRandomFloat(2, 5)
            bidet = self.randomutil.getRandomBoolean(0.5)
            selfCleaning = self.randomutil.getRandomBoolean(0.5)
            jsonobj = {
                "toiletunit-specs": {
                    "unitvolume": "{}".format(volume),
                    "unitweight": "{}".format(weight),
                    "features": {
                        "bidet": "{}".format(bidet),
                        "self-cleaning": "{}".format(selfCleaning)
                    }
                }
            }
            toiletspecs = json.dumps(jsonobj)
            stmt = 'INSERT INTO toiletunit (unitid, registration, teamid, cost, manufacturingtime, material, capacity, flowrate, toiletspecs) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(
                unitid, plane, team, cost, manufacturingtime, material, capacity, flowrate, toiletspecs
            )
            self.cursor.execute(stmt)
        self.conn.commit()

    def generateBarUnits(self, amount):
        self.cursor.execute("SELECT registration FROM plane;")
        planes = self.cursor.fetchall()

        self.cursor.execute("SELECT teamid FROM manufacturingteam;")
        teams = self.cursor.fetchall()

        for i in range(amount):
            unitid = self.randomutil.createUUID()
            plane  = choice(planes)[0]
            team = choice(teams)[0]
            cost = self.randomutil.getRandomFloat(20000, 150000)
            manufacturingtime = self.randomutil.getRandomTime()
            material = self.randomutil.getRandomMaterial()
            volume = self.randomutil.getRandomFloat(3, 15)
            weight = self.randomutil.getRandomFloat(100, 500)
            jsonobj = {
                "barunit-features": {
                    "minifridges": {
                        "amount": "{}".format(self.randomutil.getRandomInteger(5, 10)),
                        "color": "{}".format(self.randomutil.getRandomColor()),
                        "glass-door": "{}".format(self.randomutil.getRandomBoolean(0.5))
                    },
                    "glasses": {
                        "type": "{}".format(self.randomutil.getRandomGlass()),
                        "amount": "{}".format(self.randomutil.getRandomInteger(10, 100))
                    },
                    "included-auto-butler": "{}".format(self.randomutil.getRandomBoolean(0.1))
                }
            }
            features = json.dumps(jsonobj)

            stmt = 'INSERT INTO barunit (unitid, registration, teamid, cost, manufacturingtime, material, unitvolume, unitweight, features) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(
                unitid, plane, team, cost, manufacturingtime, material, volume, weight, features
            )
            self.cursor.execute(stmt)
        self.conn.commit()

    def generateBeverages(self, amount):
        self.cursor.execute("SELECT unitid FROM barunit;")
        barunits = self.cursor.fetchall()

        for i in range(amount):
            unitid = choice(barunits)[0]
            bottleid = self.randomutil.createRandomString(10)
            beverage = self.randomutil.getRandomAlcohol()
            beveragename = beverage[2]
            beveragepercentage = beverage[4]
            beveragetype = beverage[0]
            beveragecost = beverage[5]
            beveragesize = beverage[3]

            stmt = 'INSERT INTO beverage (unitid, bottleid, beveragename, beveragepercentage, beveragetype, cost, size) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(
                unitid, bottleid, beveragename, beveragepercentage, beveragetype, beveragecost, beveragesize
            )
            self.cursor.execute(stmt)
        self.conn.commit()

    def generateTestProtocols(self, amount):
        self.cursor.execute("SELECT registration FROM plane;")
        planes = self.cursor.fetchall()
        
        for i in range(amount):
            plane = choice(planes)[0]
            protocolid = self.randomutil.createRandomString(10)
            testdate = self.randomutil.getRandomDate(datetime(2015, 1, 1), datetime(2022, 3, 1))
            testroute = self.randomutil.getRandomRoute()
            testtest = self.randomutil.getRandomTest()
            testaiport = self.randomutil.createRandomString(3)
            testpilot = self.randomutil.getRandomFirstname() + " " + self.randomutil.getRandomLastname()

            results = '<results><test>{}</test><occurrences><vibrations>low</vibrations><brokeninstrument>none</brokeninstrument><detached-wing>none</detached-wing></occurrences></results>'.format(testtest)

            stmt = "INSERT INTO testprotocol (registration, protocolid, testdate, testroute, airport, pilot, results) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');".format(
                plane, protocolid, testdate, testroute, testaiport, testpilot, results
            )
            self.cursor.execute(stmt)
        self.conn.commit()


    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost", database="iop", user="paul", password="password"
            )

            self.cursor = self.conn.cursor()

            self.cursor.execute("SELECT version();")

            # display the PostgreSQL database server version
            db_version = self.cursor.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            # cursor.close()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print("Database connect closed.")

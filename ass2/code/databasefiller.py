from random import choice

from pyparsing import col
from randomutil import RandomUtil
import psycopg2


class DatabaseFiller:
    def __init__(self):
        self.randomutil = RandomUtil()
        self.conn = None
        self.connect()

    def generateCountries(self):
        countries = self.randomutil.countries
        stmt = 'INSERT INTO country (iso_code, countryname, sanctioned, currency, tariff, billionaires) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}, {});'.format(
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
            stmt = 'INSERT INTO country (iso_code, countryname, sanctioned, currency, tariff, billionaires) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}, {});'.format(
                isoCode, countryName, sanctioned, currency, tariff, billionaires
            )
            self.cursor.execute(stmt)
        self.conn.commit()
            
    def generateCustomers(self, amount):
        for i in range(amount):
            firstname = self.randomutil.getRandomFirstname()
            lastname = self.randomutil.getRandomLastname()
            birthday = self.randomutil.getRandomBirthday()
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
            seats = self.randomutil.getRandomInteger(10, 300)
            windows = self.randomutil.getRandomInteger(10, 120)

            stmt = 'INSERT INTO plane (registration, customerid, planename, color, livery, seats, numwindows) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(
                registration, customer, planename, color, livery, seats, windows
            )
            self.cursor.execute(stmt)
        self.conn.commit()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost", database="iop", user="paul", password="password"
            )

            self.cursor = self.conn.cursor()

            self.cursor.execute("SELECT version()")

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

from audioop import add
from codecs import lookup
import csv
from random import choice, random
from secrets import randbits
import numpy as np
from faker import Faker
from datetime import datetime
import uuid

class RandomUtil:
    
    firstnameFile = "./resources/firstnames.csv"
    lastnameFile = "./resources/lastnames.csv"
    streetsFile = "./resources/streets.csv"
    countriesFile = "./resources/countries.csv"
    countryLookupFile = "./resources/countrylookup.csv"

    def __init__(self):
        with open(self.firstnameFile) as file:
            self.firstnames = list(csv.reader(file))
            file.close()
        with open(self.lastnameFile) as file:
            self.lastnames = list(csv.reader(file))
            file.close()
        with open(self.streetsFile) as file:
            self.streets = np.genfromtxt(file, dtype=str, delimiter=";")
            file.close()
        with open(self.countriesFile) as file:
            self.countries = np.genfromtxt(file, dtype=str, delimiter=";")
            file.close()
        with open(self.countryLookupFile) as file:
            self.countryLookup = dict(csv.reader(file, delimiter=";"))
            file.close()

        self.faker = Faker()

    def createUUID(self):
        return str(uuid.uuid4())

    def getRandomBoolean(self, probability):
        return random() < probability

    def getRandomFirstname(self):
        return choice(self.firstnames)[0]

    def getRandomLastname(self):
        return choice(self.lastnames)[0]

    def getRandomAddress(self):
        street = self.faker.street_name()
        housenumber = self.getRandomInteger(1, 500)
        zipCode = self.faker.postcode()
        city = self.faker.city()
        country_code = self.faker.country_code()
        if country_code in self.countryLookup:
            country = self.countryLookup[country_code]
        else:
            country = "XX"
        address = [street, housenumber, zipCode, city, country, country_code]
        return address

    def getRandomInteger(self, min, max):
        return np.random.randint(min, max)

    def getRandomFloat(self, min, max):
        return round((max - min) * np.random.random_sample() + min, 2)

    def getRandomCountryCode(self):
        return choice(self.countries)[1]

    def getRandomBirthday(self):
        return self.faker.date_between_dates(date_start=datetime(1940,1,1), date_end=datetime(2000,1,1))
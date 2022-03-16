import csv
from random import choice, random
import string
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
    alcoholsFile = "./resources/alcohol_min.csv"
    upperCaseLetters = list(string.ascii_uppercase)
    numbers = [0,1,2,3,4,5,6,7,8,9]
    glasses = ["high ball", "collins", "old fashioned", "wine glass", "beer", "flute", "martini", "pint", "mug"]
    liveries = ["bare metal", "cheatline", "hockey stick", "all-over color", "eurowhite", "jelly bean", "billboard", "retro"]
    materials = ["wood", "gold", "plastic", "leather", "frottee", "metal", "chrome", "steel"]
    routes = ["open sea", "mountains", "desert", "alps", "scenic", "sketchy", "forests", "fields"]
    tests = ["high-g", "instrument", "barrel-roll", "looping", "engine", "structural-integrity", "wings", "pimp-status"]

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
        with open(self.alcoholsFile) as file:
            self.alcohols = list(csv.reader(file, delimiter=","))
            file.close()

        self.faker = Faker()

    def createRandomString(self, len):
        returnString = ""
        for i in range(len):
            returnString = returnString + choice(self.upperCaseLetters)
        return returnString

    def createRandomNumberString(self, len):
        returnString = ""
        for i in range(len):
            returnString = returnString + str(choice(self.numbers))
        return returnString

    def createUUID(self):
        return str(uuid.uuid4())

    def getRandomColor(self):
        return self.faker.safe_color_name()

    def getRandomLivery(self):
        return choice(self.liveries)

    def getRandomGlass(self):
        return choice(self.glasses)

    def getRandomMaterial(self):
        return choice(self.materials)

    def getRandomTime(self):
        return self.faker.time(pattern="%H:%M")

    def getRandomBoolean(self, probability):
        return random() < probability

    def getRandomFirstname(self):
        return choice(self.firstnames)[0]

    def getRandomLastname(self):
        return choice(self.lastnames)[0]

    def getRandomAlcohol(self):
        return choice(self.alcohols)

    def getRandomRoute(self):
        return choice(self.routes)

    def getRandomTest(self):
        return choice(self.tests)

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

    def getRandomDate(self, start, end):
        return self.faker.date_between_dates(date_start=start, date_end=end)
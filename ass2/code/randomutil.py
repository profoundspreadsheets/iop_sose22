import csv
from random import choice, random
from secrets import randbits
import numpy as np
from faker import Faker
from datetime import datetime

class RandomUtil:
    
    firstnameFile = "./resources/firstnames.csv"
    lastnameFile = "./resources/lastnames.csv"
    streetsFile = "./resources/streets.csv"
    countriesFile = "./resources/countries.csv"

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

        self.faker = Faker()

    def getRandomBoolean(self, probability):
        return random() < probability

    def getRandomFirstname(self):
        return choice(self.firstnames)[0]

    def getRandomLastname(self):
        return choice(self.lastnames)[0]

    def getRandomAddress(self):
        return choice(self.streets)

    def getRandomInteger(self, min, max):
        return np.random.randint(min, max)

    def getRandomBirthday(self):
        return self.faker.date_between_dates(date_start=datetime(1940,1,1), date_end=datetime(2000,1,1))
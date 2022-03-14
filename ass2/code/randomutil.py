import csv
from secrets import choice
import numpy as np

class RandomUtil:
    
    firstnameFile = "./resources/firstnames.csv"
    lastnameFile = "./resources/lastnames.csv"
    streetsFile = "./resources/streets.csv"

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

    def getRandomFirstname(self):
        return choice(self.firstnames)[0]

    def getRandomLastname(self):
        return choice(self.lastnames)[0]

    def getRandomAdress(self):
        return choice(self.streets)
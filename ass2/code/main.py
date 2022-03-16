from databasefiller import DatabaseFiller

def main():
    amountInserts = 777
    databasefiller = DatabaseFiller()
    databasefiller.generateCustomers(amountInserts)
    databasefiller.generateCountries()
    databasefiller.generateManufacturingTeams(amountInserts)
    databasefiller.generatePlanes(amountInserts)
    databasefiller.generateToiletUnits(amountInserts)
    databasefiller.generateBarUnits(amountInserts)
    databasefiller.generateBeverages(amountInserts)
    databasefiller.close()

if __name__ == "__main__":
    main()

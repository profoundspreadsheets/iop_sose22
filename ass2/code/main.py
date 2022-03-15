from databasefiller import DatabaseFiller

def main():
    databasefiller = DatabaseFiller()

    databasefiller.generateCustomers(777)
    
    databasefiller.generateCountries()

    databasefiller.generateManufacturingTeams(777)

    databasefiller.close()

if __name__ == "__main__":
    main()

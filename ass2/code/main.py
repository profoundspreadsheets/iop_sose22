from databasefiller import DatabaseFiller

def main():

    amount = 777

    databasefiller = DatabaseFiller()

    databasefiller.generateCustomers(amount)
    
    databasefiller.generateCountries()

    databasefiller.generateManufacturingTeams(amount)

    databasefiller.generatePlanes(amount)    

    databasefiller.close()

if __name__ == "__main__":
    main()

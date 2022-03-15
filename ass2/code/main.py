from databasefiller import DatabaseFiller

def main():
    databasefiller = DatabaseFiller()

    databasefiller.generateCustomers(10)

    databasefiller.close()

if __name__ == "__main__":
    main()

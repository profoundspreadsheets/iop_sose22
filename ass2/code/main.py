from databasefiller import DatabaseFiller

def main():
    databasefiller = DatabaseFiller()

    databasefiller.generateCustomers(800)

    databasefiller.close()

if __name__ == "__main__":
    main()

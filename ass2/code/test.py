from databasefiller import DatabaseFiller

def main():
    filler  = DatabaseFiller()

    #filler.generateToiletUnits(2)


    for i in range(50):
        primarykey = str(1000 + i)
        print (primarykey)


if __name__ == "__main__":
    main()
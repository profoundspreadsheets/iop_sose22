from randomutil import RandomUtil
import psycopg2


class DatabaseFiller:
    def __init__(self):
        self.randomutil = RandomUtil()
        self.conn = None
        self.connect()

    def generateCountries(self):
        countries = self.randomutil.countries
        cursor = self.conn.cursor()
        for i in countries:
            isoCode = i[1]
            countryName = i[0]
            sanctioned = self.randomutil.getRandomBoolean(0.05)
            currency = i[3]
            tariff = self.randomutil.getRandomInteger(100000, 999999)
            billionaires = self.randomutil.getRandomInteger(1, 50)
            stmt = 'INSERT INTO COUNTRY (iso_code, countryname, sanctioned, currency, tariff, billionaires) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}, {});'.format(
                isoCode, countryName, sanctioned, currency, tariff, billionaires
            )
            cursor.execute(stmt)
            self.conn.commit()
            

    def generateCustomers(self, amount):
        print("Generating {} amount of customers".format(amount))
        cursor = self.conn.cursor()

        for i in range(amount):
            firstname = self.randomutil.getRandomFirstname()
            lastname = self.randomutil.getRandomLastname()
            birthday = self.randomutil.getRandomBirthday()
            address = self.randomutil.getRandomAddress()
            housenumber = self.randomutil.getRandomInteger(1, 500)
            stmt = 'INSERT INTO CUSTOMER (firstname, lastname, birthday, street, housenumber, zip, city) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}, {}, \'{}\');'.format(
                firstname, lastname, birthday, address[0], housenumber, address[1], address[2]
            )
            cursor.execute(stmt)
            self.conn.commit()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost", database="iop", user="paul", password="password"
            )

            cursor = self.conn.cursor()

            cursor.execute("SELECT version()")

            # display the PostgreSQL database server version
            db_version = cursor.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            # cursor.close()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print("Database connect closed.")

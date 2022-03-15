from randomutil import RandomUtil
import psycopg2


class DatabaseFiller:
    def __init__(self):
        self.randomutil = RandomUtil()
        self.conn = None
        self.connect()

    def generateCountries(self):
        pass

    def generateCustomers(self, amount):
        print("Generating {} amount of customers".format(amount))
        cursor = self.conn.cursor()

        for i in range(amount):
            firstname = self.randomutil.getRandomFirstname()
            lastname = self.randomutil.getRandomLastname()
            birthday = self.randomutil.getRandomBirthday()
            address = self.randomutil.getRandomAddress()
            stmt = 'INSERT INTO customer (firstname, lastname, birthday, street, housenumber, zip) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {}, {});'.format(
                firstname, lastname, birthday, address[0], 5, address[1]
            )
            print(stmt)

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
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print("Database connect closed.")

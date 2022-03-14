import psycopg2


def main():
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="iop",
            user="paul",
            password="password"
        )

        cursor = conn.cursor()

        cursor.execute("SELECT version()")

        # display the PostgreSQL database server version
        db_version = cursor.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()
            print("Database connect closed.")


if __name__ == "__main__":
    main()

import sqlite3

dbfile='SQLite_amazon.db'

sql_create_table = """ CREATE TABLE IF NOT EXISTS amazon_prices (
                                        id integer PRIMARY KEY,
                                        curdate text NOT NULL,
                                        sku text NOT NULL,
                                        price text NOT NULL,
                                        searchterm text NOT NULL
                                    );"""

def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_table)
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")
    

def insertVaribleIntoTable(curdate, sku, price,searchterm):
    try:
        conn = sqlite3.connect(dbfile)
        create_table(conn)
        cursor = conn.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO amazon_prices
                          (curdate, sku, price,searchterm) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (curdate, sku, price,searchterm)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into amazon_prices table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
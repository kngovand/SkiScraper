import sqlite3
from sqlite3 import Error

# from https://www.sqlitetutorial.net/sqlite-python/creating-database/
conn = None
try:
    conn = sqlite3.connect(r'C:\Users\Admin\Desktop\Code\SkiScraper\scraper\pythonsqlite.db')
    print('Version: ' + sqlite3.version + '... working!')

    cursor = conn.cursor()

    create_copper = """
    CREATE TABLE data_cp (
        id INTEGER PRIMARY KEY,
        temp INTEGER,
        depth1 INTEGER,
        depth2 INTEGER,
        lifts INTEGER,
        trails INTEGER
    );
    """

    create_wp = """
    CREATE TABLE data_wp (
        id INTEGER PRIMARY KEY,
        temp INTEGER,
        depth1 INTEGER,
        depth2 INTEGER,
        lifts INTEGER,
        trails INTEGER
    );
    """

    cursor.execute(create_copper)
    print('Copper table successful')
    cursor.execute(create_wp)
    print('WP table successful')

    insert_test = """INSERT INTO data_wp VALUES (1, 2, 3, 4, 5, 6);"""
    cursor.execute(insert_test)
    cursor.execute("""select * from data_wp """)
    #test select output
    print(cursor.fetchone())

except Error as e:
    print(e)
finally:
    if conn:
        conn.close()



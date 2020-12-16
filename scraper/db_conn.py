import sqlite3
from sqlite3 import Error

# from https://www.sqlitetutorial.net/sqlite-python/creating-database/
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Version: ' + sqlite3.version + '... working!')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r'C:\Users\Admin\Desktop\Code\SkiScraper\scraper\pythonsqlite.db') 
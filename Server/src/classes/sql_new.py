import sqlite3

from sql import auslesen, insert

try:
    sqliteCon = sqlite3.connect('Datebase_python.db')
    query_create_table = 	'''CREATE TABLE Protokoll (
                                id INTEGER NOT NULL,
                                Zeit TEXT NOT NULL,
				Datum TEXT NOT NULL,
                                Status BOOLEAN);'''

    cursor = sqliteCon.cursor()
    print("Connected to the database")
    cursor.execute(query_create_table)
    sqliteCon.commit()
    print("Database created")
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating the table - ", error)
	
finally:
    if (sqliteCon):
        sqliteCon.close()
        print("database connection is closed")
    auslesen(1)
    
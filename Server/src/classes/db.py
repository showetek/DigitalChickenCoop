import sqlite3


class db_connector():


    def start(database):
        sqlite3.connect(database)




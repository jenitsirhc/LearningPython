import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database connected/created")

except sqlite3.Error as error:
    print("Error while connecting to sqlite")

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
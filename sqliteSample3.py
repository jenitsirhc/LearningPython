import sqlite3



try:

  sqliteConnection = sqlite3.connect('SQLite_Python.db')
  cursor = sqliteConnection.cursor()
  sqlite_insert_query = '''INSERT INTO SqliteDb_developers (

                'id', 'name', 'email', 'joining_date', 'salary')
                VALUES(1, 'James', 'james@pynative.com','2019-03-17', 8000)'''



  count = cursor.execute(sqlite_insert_query)

  sqliteConnection.commit()

  print("Record inserted successfully into SqliteDB_developers table", cursor.rowcount)

  cursor.close()



except sqlite3.Error as error:

  print("Error while creating a sqlite table", error)

finally:

  if sqliteConnection:

    sqliteConnection.close()

    print("sqlite connection is closed")
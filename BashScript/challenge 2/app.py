import sqlite3
import sys

def connectDb():
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    return cursor,sqliteConnection

def createTable(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE info(first_name text , second_name text, phone_num int PRIMARY KEY, department text, salary int)")
    con.commit()
    print ("database is created sussessfully")

def insertRecord(record , cursor ,sqliteConnection ):
    sqlite_insert_query = """INSERT INTO info
                          (first_name, second_name, phone_num, department, salary) 
                           VALUES (?, ?, ?, ?, ?);"""
    data_tuple = (record[0], record[1], record[2], record[3], record[4])
    cursor.execute(sqlite_insert_query, data_tuple)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

    return ""

def validateInput(InputArgument):
    if len(InputArgument[2]) != 11:
        print("your number must be at least 11 number")
    elif (isinstance(InputArgument[0], str) != True):
        print("please enter valid name first name must be string")
    elif (isinstance(InputArgument[1], str)!= True):
        print("please enter valid name second name must be string")  
    elif (isinstance(InputArgument[3], str)!= True):
        print("department must be string")
    elif (isinstance(InputArgument[4], str)!= True):
        print("salary must be int")               
    else:
        cursor,sqliteConnection = connectDb()
        insertRecord(InputArgument , cursor ,sqliteConnection)


if __name__ == "__main__":
    validateInput(sys.argv[1:])
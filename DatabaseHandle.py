import sqlite3 as sl


def CreateDatabase():
    con = sl.connect('my-test.db')
    with con:
        con.execute("""
            CREATE TABLE Accounts (
                email TEXT,
                password TEXT,
                username TEXT,
                url TEXT,
                app_name TEXT

            );
        """)

def InsertEntry(email,password,username,url,app_name):
    con = sl.connect('my-test.db')
    sql = 'INSERT INTO Accounts (email,password,username,url,app_name) values(?, ?, ?, ?, ?)'
    data = [
        ('email','password','username','url','app_name')
    ]
    with con:
        con.executemany(sql, data)

def DeleteRecords():
    con = sl.connect('my-test.db')
    with con:
        con.execute("""
        Delete from Accounts;
        """)
    print("All entries deleted")
    print('\n\n')


def ShowValues():
    con = sl.connect('my-test.db')
    with con:
        data = con.execute("SELECT * FROM Accounts")
        for row in data:
            print(row)
    input("press enter to continue!!!!")
    print('\n\n')
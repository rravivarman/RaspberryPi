import sqlite3
import os


def add_card(cardNo,expDate,pinNo):
    db_filename = 'cartdata.db'
    db_exists = not os.path.exists(db_filename)
    conn = sqlite3.connect(db_filename)
    if db_exists:
        print('No schema exists.')
    else:
        c=conn.cursor()
        c.execute('SELECT * FROM card WHERE cardno = :word', {"word": cardNo})
        data = c.fetchone()
        if data is not None:
            print("Card Already Exists")
            #print(data)
        else:
            
            c.execute("""INSERT INTO card(cardno,expiry,pin) VALUES((?), (?), (?))""", (cardNo,expDate,pinNo))
            conn.commit()
            c.execute('SELECT * FROM card WHERE cardno = :word', {"word": cardNo})
            data = c.fetchone()
            if data is not None:
                print("Card Data Added")
            else:
                print("Card Data Not Added")
                #print(data)
    conn.close()

def check_card(cardNo):
    db_filename = 'cartdata.db'
    db_exists = not os.path.exists(db_filename)
    conn = sqlite3.connect(db_filename)
    conn.row_factory = dict_factory
    if db_exists:
        print('No schema exists.')
    else:
        c=conn.cursor()
        c.execute('SELECT cardno FROM card WHERE cardno = :word', {"word": cardNo})
        data = c.fetchone()
        if data is not None:
            print("Card Exists")
            print(data)
        else:
            print("Card Not Exists")
            #print(data)
            
    conn.close()

def dict_factory(cursor, row):
    d = 0
    for idx, col in enumerate(cursor.description):
        d = row[0]
    return d

def deleteRecord(cardno):
    try:
        sqliteConnection = sqlite3.connect('cartdata.db')
        cursor = sqliteConnection.cursor()
        cursor.execute('DELETE FROM card WHERE cardno = :word', {"word": cardno})
        sqliteConnection.commit()
        cursor.close()
        print("Card Deleted")
    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


n = ''#12345677
e = ''#'12/22'
p = ''#123

#add_card(n,e,p);
#check_card(n)
deleteRecord(n)
check_card(n)

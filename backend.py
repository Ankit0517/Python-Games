import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , ipl integer , exercise text , study text , cricket text ,python text)")
    conn.commit()
    conn.close()

def insert(date , ipl , exercise , study , cricket , python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date , ipl , exercise , study , cricket , python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , ipl='' , exercise='' , study='' , cricket='' , python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR ipl=? OR exercise=? OR study=? OR cricket=? OR python=?" , (date , ipl , exercise , study , cricket , python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()

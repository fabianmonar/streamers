import sqlite3  as sql

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()
    
    
def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers(
            name text,
            followers integer,
            subs integer 
        
        )"""
        
    )
    conn.commit()
    conn.close()
    
def insertRow(nombre, followers, subs):
     conn = sql.connect("streamers.db")
     cursor = conn.cursor()
     instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
     cursor.execute(instruccion)
     conn.commit()
     conn.close()
    
def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def insertRows(streamerList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()
    
def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers  WHERE name='AlexElcapo'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def updateFields():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers=12000000 WHERE name like 'elxokas'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
   

    
if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow("Ibai", 7000000, 25000)
    #insertRow("AlexElcapo", 800000, 5000)
    #readRows()
    streamers = [
        ("Elxokas", 1000000, 9500),
        ("Cristinini", 3000000, 5500),
        ("Auronplay", 8000000, 2000)
    ]
    #insertRows(streamers)
    #readOrdered("subs")
    #search()
    updateFields()
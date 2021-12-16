import sqlite3 as lite
from datetime import date
import sys
con = lite.connect('sensorsData.db')
with con:
    cur =con.cursor()
    cur.execute("DROP TABLE IF EXISTS Shelf_life")
    cur.execute("CREATE TABLE Shelf_life(timestamp DATE,name TEXT ,shelf DATE)")


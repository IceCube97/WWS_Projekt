"""
import sqlite3

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect('wws.db')

# Datensatzcursor erzeugen
# Merke: cursor wird benötigt, um SQL-Anweisungen später ausführen zu können
cursor = connection.cursor()

# Tabelle erzeugen
sql = ' CREATE TABLE artikel (' \
      'art_nr INTEGER PRIMARY KEY,' \
      'art_bez TEXT,' \
      'art_bestand TEXT,' \
      'art_mhd DATE)'

cursor.execute(sql)
"""



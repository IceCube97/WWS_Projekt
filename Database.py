"""
# 2.1.Datenbankdatei erstellen
# ausgeführt am 28.04.2023

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

"""import sqlite3

connection = sqlite3.connect('wws.db')
cursor = connection.cursor()
sql = 'ALTER TABLE artikel ADD COLUMN art_mhd DATE'
cursor.execute(sql)"""


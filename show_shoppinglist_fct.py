import sqlite3
import tkinter as tk


def show_shoppinglist_fct():
    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('wws.db')
    cursor = connection.cursor()

    # SQL-Abfrage, um Artikel mit Bestand <= 1 abzurufen
    sql = 'SELECT art_bez FROM artikel WHERE art_bestand <= 1 ORDER BY art_bez ASC'

    # SQL-Abfrage ausführen und Ergebnisse abrufen
    cursor.execute(sql)
    results = cursor.fetchall()

    # Verbindung zur Datenbank schließen
    connection.close()

    # Ergebnisse sortieren und als Liste speichern
    shoppinglist = sorted([row[0] for row in results])

    # Tkinter-Fenster erzeugen
    window = tk.Tk()
    window.title("Einkaufsliste")
    window.geometry('400x300')

    # Listbox erzeugen und Ergebnisse einfügen
    listbox = tk.Listbox(window)
    for artikel in shoppinglist:
        listbox.insert(tk.END, artikel)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Tkinter-Fenster starten
    window.mainloop()





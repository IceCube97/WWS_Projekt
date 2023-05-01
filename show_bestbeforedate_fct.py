import tkinter
import sqlite3


def show_bestbeforedate_fct():
    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('wws.db')
    cursor = connection.cursor()

    # Query vorbereiten, um Artikel mit art_mhd innerhalb der nächsten 5 Tagen zu bekommen
    sql = "SELECT * FROM artikel WHERE date(art_mhd) BETWEEN date('now') AND date('now', '+5 days') ORDER BY art_bez"

    # Query ausführen und Ergebnisse speichern
    cursor.execute(sql)
    rows = cursor.fetchall()

    # Neues Fenster erstellen und Konfigurationen setzen
    window = tkinter.Toplevel()
    window.geometry('350x350')
    window.title('MHD-Liste')
    window.resizable(False, False)

    # Label und Listbox im Fenster erstellen
    label = tkinter.Label(window, text='Artikel mit MHD innerhalb der nächsten 5 Tage:')
    label.pack(pady=10)

    listbox = tkinter.Listbox(window, width=50)
    listbox.pack()

    # Ergebnisse in der Listbox anzeigen
    for row in rows:
        listbox.insert(tkinter.END, f"{row[1]} - MHD: {row[3]}")

    # Verbindung zur Datenbank schließen
    connection.close()

import sqlite3
import tkinter
import tkinter.ttk as ttk

def show_database_fct():
    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('wws.db')
    cursor = connection.cursor()

    # Tabelle aus der Datenbank abrufen
    cursor.execute('SELECT * FROM artikel ORDER BY art_bez ASC')
    data = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]  # Spaltennamen abrufen

    # Ein neues Fenster für die Datenbank erstellen
    db_window = tkinter.Toplevel()
    db_window.title("Datenbank anzeigen")
    db_window.geometry('820x300')

    # Treeview erstellen
    treeview = ttk.Treeview(db_window, columns=column_names, show='headings')
    treeview.grid(row=0, column=0, sticky='nsew')

    # Spaltennamen im Treeview anzeigen
    for name in column_names:
        treeview.heading(name, text=name)

    # Daten in Treeview einfügen
    for row in data:
        treeview.insert('', 'end', values=row)

    # Zeige das Fenster an und blockiere das Hauptfenster, bis es geschlossen wird
    db_window.wait_window()

    # Verbindung zur Datenbank schließen
    connection.close()



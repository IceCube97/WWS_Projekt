import sqlite3
import tkinter


def show_database_fct():
    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('wws.db')
    cursor = connection.cursor()

    # Tabelle aus der Datenbank abrufen
    cursor.execute("SELECT * FROM artikel")
    data = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]  # Spaltennamen abrufen

    # Ein neues Fenster für die Datenbank erstellen
    db_window = tkinter.Toplevel()
    db_window.title("Datenbank anzeigen")
    db_window.geometry('600x500')

    # Spaltennamen im Fenster anzeigen
    for j, name in enumerate(column_names):
        label = tkinter.Label(db_window, text=name, font=("Arial", 12, "bold"), borderwidth=2, relief="solid")
        label.grid(row=0, column=j, padx=5, pady=5)

    # Tabelle für die Datenbank im Fenster anzeigen
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            label = tkinter.Label(db_window, text=value, borderwidth=2, relief="solid")
            label.grid(row=i+1, column=j, padx=5, pady=5)

    # Zeige das Fenster an und blockiere das Hauptfenster, bis es geschlossen wird
    db_window.wait_window()

    # Verbindung zur Datenbank schließen
    connection.close()


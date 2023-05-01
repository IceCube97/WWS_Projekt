import tkinter as tk
import sqlite3
import tkinter.ttk


def bestand_aendern_fct():
    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('wws.db')
    cursor = connection.cursor()

    # SQL-Abfrage, um die Artikel alphabetisch zu sortieren
    sql = 'SELECT * FROM artikel ORDER BY art_bez ASC'
    cursor.execute(sql)
    rows = cursor.fetchall()

    # neues Fenster erstellen
    bestand_aendern_window = tk.Toplevel()
    bestand_aendern_window.title('Bestand ändern')

    # Treeview erstellen
    columns = ('Artikelnummer', 'Bezeichnung', 'Bestand', 'MHD')
    treeview = tk.ttk.Treeview(bestand_aendern_window, columns=columns, show='headings')
    for col in columns:
        treeview.heading(col, text=col)
    treeview.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Daten in Treeview einfügen
    for row in rows:
        treeview.insert('', 'end', values=row)

    # Funktion, um den Bestand zu ändern
    def change_bestand():
        selection = treeview.selection()
        if selection:
            artikel_nr = treeview.item(selection[0])['values'][0]
            new_bestand = int(bestand_entry.get())
            sql = f"UPDATE artikel SET art_bestand = {new_bestand} WHERE art_nr = {artikel_nr}"
            cursor.execute(sql)
            connection.commit()
            # Daten in Treeview aktualisieren
            treeview.item(selection[0], values=(artikel_nr, treeview.item(selection[0])['values'][1], new_bestand,
                                                treeview.item(selection[0])['values'][3]))

    # Label und Eingabefeld für den neuen Bestand erstellen
    bestand_label = tk.Label(bestand_aendern_window, text='Neuer Bestand:')
    bestand_label.grid(row=1, column=0, padx=10, pady=10)

    bestand_entry = tk.Entry(bestand_aendern_window)
    bestand_entry.grid(row=1, column=1, padx=10, pady=10)

    # Button zum Speichern des neuen Bestands erstellen
    save_button = tk.Button(bestand_aendern_window, text='Speichern', command=change_bestand)
    save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

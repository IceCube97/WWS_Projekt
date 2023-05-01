import sqlite3
import tkinter
from tkinter import messagebox


def delete_article_fct():
    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('wws.db')
    cursor = connection.cursor()

    # Tabelle aus der Datenbank abrufen
    cursor.execute("SELECT * FROM artikel")
    data = cursor.fetchall()

    # Ein neues Fenster für die Löschfunktion erstellen
    delete_window = tkinter.Toplevel()
    delete_window.title("Artikel löschen (Artikel alphabetisch sortiert)")
    delete_window.geometry('500x500')

    # Liste der Artikel im Fenster anzeigen
    items = [item[1] for item in data]
    items.sort()
    listbox = tkinter.Listbox(delete_window, width=50)
    for item in items:
        listbox.insert(tkinter.END, item)
    listbox.pack(pady=10)

    # Funktion für das Löschen des Artikels definieren
    def delete_item():
        selection = listbox.curselection()
        if selection:
            item_index = selection[0]
            item_name = listbox.get(item_index)
            response = messagebox.askyesno("Artikel löschen", f"Möchten Sie den Artikel '{item_name}' wirklich löschen?")
            if response == tkinter.YES:
                cursor.execute("DELETE FROM artikel WHERE art_bez = ?", (item_name,))
                connection.commit()
                messagebox.showinfo("Artikel gelöscht", f"Der Artikel '{item_name}' wurde erfolgreich aus der Datenbank gelöscht.")
                listbox.delete(item_index)

    # Button zum Löschen des Artikels hinzufügen
    button_delete = tkinter.Button(delete_window, text="Löschen", command=delete_item)
    button_delete.pack(pady=10)

    # Zeige das Fenster an und blockiere das Hauptfenster, bis es geschlossen wird
    delete_window.wait_window()

    # Verbindung zur Datenbank schließen
    connection.close()

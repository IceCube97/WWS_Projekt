import tkinter
import tkinter.messagebox
import sqlite3
import re


def add_article_fct():
    # Funktion wird aufgerufen, wenn der Button "Artikel Hinzufügen" gedrückt wird

    # neues Fenster erstellen
    add_article_window = tkinter.Toplevel()
    add_article_window.geometry('350x200')
    add_article_window.title('Artikel hinzufügen')
    add_article_window.resizable(False, False)

    # Label und Textbox für die Artikelbezeichnung
    label_art_bez = tkinter.Label(add_article_window, text='Artikelbezeichnung')
    label_art_bez.grid(column=0, row=0, padx=10, pady=10)

    textbox_art_bez = tkinter.Entry(add_article_window, width=30)
    textbox_art_bez.grid(column=1, row=0, padx=10, pady=10)

    # Label und Textbox für den Bestand
    label_art_bestand = tkinter.Label(add_article_window, text='Bestand:')
    label_art_bestand.grid(column=0, row=1, padx=10, pady=10)

    textbox_art_bestand = tkinter.Entry(add_article_window, width=30)
    textbox_art_bestand.grid(column=1, row=1, padx=10, pady=10)

    # Label und Textbox für das MHD
    label_art_mhd = tkinter.Label(add_article_window, text='Mindesthaltbarkeitsdatum:')
    label_art_mhd.grid(column=0, row=2, padx=10, pady=10)

    textbox_art_mhd = tkinter.Entry(add_article_window, width=30)
    textbox_art_mhd.grid(column=1, row=2, padx=10, pady=10)

    # Button zum Hinzufügen des Artikels
    def add_article_to_database():
        # Daten aus den Textboxen auslesen
        art_bez = textbox_art_bez.get()
        art_bestand = textbox_art_bestand.get()
        art_mhd = textbox_art_mhd.get()

        # Exception-handling für den Bestand
        try:
            art_bestand = int(art_bestand)
            if art_bestand < 0:
                raise ValueError
        except ValueError:
            tkinter.messagebox.showerror('Fehler', 'Der Bestand muss eine positive ganze Zahl sein.')
            return

        # Überprüfen, ob eine Artikelbezeichnung eingegeben wurde
        try:
            if len(art_bez) < 3:
                raise ValueError('Artikelbezeichnung fehlt, min. 3 Buchstaben.')
        except ValueError as e:
            tkinter.messagebox.showerror('Fehler', str(e))
            return

        # Exception-handling für das MHD
        try:
            if art_mhd and not re.match(r'^\d{4}-\d{2}-\d{2}$', art_mhd):
                raise ValueError('MHD muss im Format YYYY-MM-DD eingegeben werden.')
        except ValueError as e:
            tkinter.messagebox.showerror('Fehler', str(e))
            return

        # Verbindung zur Datenbank herstellen
        connection = sqlite3.connect('wws.db')
        cursor = connection.cursor()

        # neuen Datensatz in die Datenbank einfügen
        cursor.execute('INSERT INTO artikel (art_bez, art_bestand, art_mhd) VALUES (?, ?, ?)',
                       (art_bez, art_bestand, art_mhd))
        connection.commit()

        # Datenbankverbindung schließen
        cursor.close()
        connection.close()

        # Meldung ausgeben, dass der Artikel hinzugefügt wurde
        tkinter.messagebox.showinfo('Erfolg', 'Der Artikel wurde erfolgreich hinzugefügt.')

        # Textboxen leeren
        textbox_art_bez.delete(0, 'end')
        textbox_art_bestand.delete(0, 'end')
        textbox_art_mhd.delete(0, 'end')

    button_add_article = tkinter.Button(add_article_window, text='Artikel hinzufügen',
                                        width=20, height=2, command=add_article_to_database)
    button_add_article.grid(column=1, row=3, padx=10, pady=10)

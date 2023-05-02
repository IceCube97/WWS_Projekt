# Mein WWS - Projekt
# Start: 27.04.2023
# ______________________________________________________________________________________________________________________
import tkinter

import show_bestbeforedate_fct
import show_database_fct  # Erstellt am 28.04.2023
import add_article_fct  # Erstellt am 28.04.2023
import delete_article_fct  # Erstellt am 28.04.2023
import show_shoppinglist_fct  # Erstellt am 29.04.2023
import bestand_aendern_fct  # Erstellt am 29.04.2023

# Hauptfenster erstellt am 27.04.2023
main = tkinter.Tk()
main.geometry('350x350')
main.title('Mini-WWS')
main.resizable(False, False)

# Buttons im Hauptfenster erstellt am 27.04.2023
button_width = 20
button_height = 4


button_show_database = tkinter.Button(main, text='Datenbank anzeigen',
                                      width=button_width, height=button_height,
                                      command=show_database_fct.show_database_fct)
button_show_database.grid(column=0, row=0, padx=10, pady=10)

button_add_article = tkinter.Button(main, text='Artikel hinzufügen',
                                    width=button_width, height=button_height,
                                    command=add_article_fct.add_article_fct)
button_add_article.grid(column=0, row=1, padx=10, pady=20)

button_delete_article = tkinter.Button(main, text='Artikel löschen',
                                       width=button_width, height=button_height,
                                       command=delete_article_fct.delete_article_fct)
button_delete_article.grid(column=0, row=2, padx=10, pady=20)

button_show_shoppinglist = tkinter.Button(main, text='Einkaufsliste',
                                          width=button_width, height=button_height,
                                          command=show_shoppinglist_fct.show_shoppinglist_fct)
button_show_shoppinglist.grid(column=1, row=0, padx=10, pady=20)

button_bestand_aendern = tkinter.Button(main, text='Bestand bestehender \n Artikel aendern',
                                        width=button_width, height=button_height,
                                        command=bestand_aendern_fct.bestand_aendern_fct)
button_bestand_aendern.grid(column=1, row=1, padx=10, pady=20)

button_show_bestbeforedate = tkinter.Button(main, text='MHD-Liste',
                                            width=button_width, height=button_height,
                                            command=show_bestbeforedate_fct.show_bestbeforedate_fct)
button_show_bestbeforedate.grid(column=1, row=2, padx=10, pady=20)

main.mainloop()

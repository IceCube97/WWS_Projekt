# WWS_Projekt
This is my first own project. I can track my Inventory, stuff I need to buy regulary, like food or snacks for my dog. 
So i do not need to look everything up and write a shoppinglist everytime I go to the grocery store. 
It's like a "Mini-Inventory-Management-System".
Here, I'm trying to explain what my program does:

"Oberflaeche.py" is the main-window where you can see 6 buttons:
  - "Datenbank anzeigen"                    : show the database;                                     function for this button -> "show_database_fct.py"
  - "Artikel hinzufügen"                    : add article (to the database);                         function for this button -> "add_article_fct.py"
  - "Artikel löschen"                       : delete article (from the database);                    function for this button -> "delete_article_fct.py"
  - "Einkaufsliste"                         : Shopping-list;                                         function for this button -> "show_shoppinglist_fct.py"
  - "Bestand bestehender Artikel ändern "   : change the number of the articles in the database;     function for this button -> "bestand_aendern_fct.py"
  - "MHD-Liste"                             : the best-before-date - list;                           function for this button -> "show_bestbeforedate_fct.py"

Explanation of the functionality of these 6 buttons:

  - "Datenbank anzeigen"                    : It will show you the whole inventory (the whole database "wws.db", it has one table yet)
  - "Artikel hinzufügen"                    : You can add a new article to the database, where you have to type in the item description, the stock, and the best-before-date
  - "Artikel löschen"                       : It will show you an alphabetical ordered list of the inventory. You can klick on the item you want to delete from the database
  - "Einkaufsliste"                         : That button will give you the shopping-list. A list of items appears whose inventory is less than or equal to one.
  - "Bestand bestehender Artikel ändern"    : It will show you an alphabetical ordered list of the inventory. You can also click the item and change the stock.
  - "MHD-Liste"                             : You get a list of items whose best before date expires in the next 5 days. (Thought it would be handy to see which foods should be consumed first.)

Database.py
  - How my database looks like 


This is the "main-functionality" I want. But I got already some ideas of extending the database and adding / changing some functionalities.

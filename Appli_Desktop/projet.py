# -- coding: utf-8 --
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    

    def _init_(self):
        
        Gtk.Window._init_(self, title="Hotel TERANGA")
        

        # Création de la barre d'en-tête
        headerbar = Gtk.HeaderBar()
        headerbar.set_show_close_button(True)
        headerbar.props.title = "Hotel TERANGA"
        self.set_titlebar(headerbar)
        # Définition de l'image d'arrière-plan
        image = Gtk.Image()
        image.set_from_file("C:\Users\LENOVO\Desktop\pythproject/hotel_teranga.jpeg")
        self.add(image)

        # Création de la boîte principale
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        # Création du bouton "Client"
        self.button_client = Gtk.Button(label="Client")
        self.button_client.connect("clicked", self.on_client_clicked)
        headerbar.pack_start(self.button_client)

        # Création du bouton "Chambre"
        self.button_chambre = Gtk.Button(label="Chambre")
        self.button_chambre.connect("clicked", self.on_chambre_clicked)
        headerbar.pack_start(self.button_chambre)

        # Création du bouton "Réservation"
        self.button_Reservation = Gtk.Button(label="Reservation")
        self.button_Reservation.connect("clicked", self.on_reservation_clicked)
        headerbar.pack_start(self.button_Reservation)

        # Création du bouton "Facture"
        self.button_facture = Gtk.Button(label="Facture")
        headerbar.pack_end(self.button_facture)

        # Création du bouton "Statistiques"
        self.button_statistiques = Gtk.Button(label="Statistiques")
        self.button_statistiques.connect("clicked", self.on_statistiques_clicked)
        headerbar.pack_end(self.button_statistiques)




        
    def on_client_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour les options de chambre
        win = Gtk.Window(title="Options de client")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(200, 100)

        # Création de la boîte pour le formulaire
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        win.add(box)

        # Ajout des boutons pour les différentes options
        button_ajout_client = Gtk.Button(label="Ajouter Client")
        button_ajout_client.connect("clicked", self.on_ajout_client_clicked)
        box.pack_start(button_ajout_client, True, True, 0)

        button_liste_client = Gtk.Button(label="Liste des clients de l'hotel")
        button_liste_client.connect("clicked", self.on_liste_client_clicked)
        box.pack_start(button_liste_client, True, True, 0)

        button_liste_present = Gtk.Button(label="Liste des clients présents")
        button_liste_present.connect("clicked", self.on_liste_present_clicked)
        box.pack_start(button_liste_present, True, True, 0) 
        

        win.show_all()
        

        











    def on_ajout_client_clicked (self, widget):
        # Ouvrir une nouvelle fenêtre pour le formulaire du client
        win = Gtk.Window(title="Formulaire client")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(200, 100)

        # Création de la boîte pour le formulaire
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        win.add(box)

        # Ajout des champs pour le formulaire
        prenom_label = Gtk.Label("Prénom")
        box.pack_start(prenom_label, True, True, 0)
        prenom_entry = Gtk.Entry()
        box.pack_start(prenom_entry, True, True, 0)

        nom_label = Gtk.Label("Nom")
        box.pack_start(nom_label, True, True, 0)
        nom_entry = Gtk.Entry()
        box.pack_start(nom_entry, True, True, 0)

        adresse_label = Gtk.Label("Adresse")
        box.pack_start(adresse_label, True, True, 0)
        adresse_entry = Gtk.Entry()
        box.pack_start(adresse_entry, True, True, 0)

        telephone_label = Gtk.Label("Téléphone")
        box.pack_start(telephone_label, True, True, 0)
        telephone_entry = Gtk.Entry()
        box.pack_start(telephone_entry, True, True, 0)

        # Ajout du bouton "Enregistrer"
        button_enregistrer = Gtk.Button(label="Enregistrer")
        box.pack_start(button_enregistrer, True, True, 0)
        win.show_all()
        




    
    def on_chambre_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour les options de chambre
        win = Gtk.Window(title="Options de chambre")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(200, 100)

        # Création de la boîte pour les options
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        win.add(box)

        # Ajout des boutons pour les différentes options
        button_liste_chambres = Gtk.Button(label="Liste des chambres")
        button_liste_chambres.connect("clicked", self.on_liste_chambres_clicked)
        box.pack_start(button_liste_chambres, True, True, 0)

        button_chambres_occupees = Gtk.Button(label="Liste des chambres occupées")
        button_chambres_occupees.connect("clicked", self.on_chambres_occupee)
        box.pack_start(button_chambres_occupees, True, True, 0)

        button_chambres_reservees = Gtk.Button(label="Liste des chambres réservées")
        button_chambres_reservees.connect("clicked", self.on_chambres_reservees)
        box.pack_start(button_chambres_reservees, True, True, 0) 

        win.show_all()
        
        
        
    def on_reservation_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour les options de chambre
        win = Gtk.Window(title="Options de Reservation")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(200, 100)

        # Création de la boîte pour le formulaire
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        win.add(box)

        # Ajout des boutons pour les différentes options
        button_faire_reservation = Gtk.Button(label="Faire reservation")
        button_faire_reservation.connect("clicked", self.on_faire_reservation_clicked)
        box.pack_start(button_faire_reservation, True, True, 0)

        button_annuler_reservation = Gtk.Button(label="annuler_reservation")
        button_annuler_reservation.connect("clicked", self.on_annuler_reservation_clicked)
        box.pack_start(button_annuler_reservation, True, True, 0)

        win.show_all()



        

    def on_faire_reservation_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour le formulaire du client
        win = Gtk.Window(title="Formulaire reservation")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(200, 100)

        # Création de la boîte pour le formulaire
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        win.add(box)

        # Ajout des champs pour le formulaire
        
        ID_client = Gtk.Label("ID_Client")
        box.pack_start(ID_client, True, True, 0)
        ID_client_entry = Gtk.Entry()
        box.pack_start(ID_client_entry, True, True, 0)
        
        Date_arrivee_label = Gtk.Label("Date_arrivee")
        box.pack_start(Date_arrivee_label, True, True, 0)
        Date_arrivee_entry = Gtk.Entry()
        box.pack_start(Date_arrivee_entry, True, True, 0)

        Date_depart_label = Gtk.Label("Date_depart")
        box.pack_start(Date_depart_label, True, True, 0)
        Date_depart_entry = Gtk.Entry()
        box.pack_start(Date_depart_entry, True, True, 0)

        Type_tarif_label = Gtk.Label("Type_tarif")
        box.pack_start(Type_tarif_label, True, True, 0)
        Type_tarif_entry = Gtk.Entry()
        box.pack_start(Type_tarif_entry, True, True, 0)
        
        num_chambre_entry = Gtk.Label("num_chambre")
        box.pack_start(num_chambre_entry, True, True, 0)
        num_chambre_entry = Gtk.Entry()
        box.pack_start(num_chambre_entry, True, True, 0)
        
        
        # Ajout du bouton "Enregistrer"
        button_enregistrer = Gtk.Button(label="Enregistrer")
        box.pack_start(button_enregistrer, True, True, 0)
        win.show_all()
        



    def on_annuler_reservation_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour le formulaire du client
        win = Gtk.Window(title="Formulaire reservation")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(200, 100)

        # Création de la boîte pour le formulaire
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        win.add(box)

        # Ajout des champs pour le formulaire
        
        ID_client = Gtk.Label("ID_Client")
        box.pack_start(ID_client, True, True, 0)
        ID_client_entry = Gtk.Entry()
        box.pack_start(ID_client_entry, True, True, 0)
        
        
        ID_reservation = Gtk.Label("ID_reservation")
        box.pack_start(ID_reservation, True, True, 0)
        ID_reservation_entry = Gtk.Entry()
        box.pack_start(ID_reservation_entry, True, True, 0)
        
        

       
        
        
        # Ajout du bouton "AnnulerS"
        button_annuler = Gtk.Button(label="Annuler")
        box.pack_start(button_annuler, True, True, 0)
        win.show_all()
        


        
    def on_liste_client_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour afficher la liste des clients
        win = Gtk.Window(title="Liste des clients de l'hôtel Teranga")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(400, 300)

        # Création du modèle de données
        liste_clients = Gtk.ListStore(str, str, str, str, str)
        # Ajouter des données de test
        liste_clients.append(["1", "SOW", "Ibrahima", "0123456789", "Dalifort"])
        liste_clients.append(["2", "DIARRA", "Abdoulaye", "0123456789", "Liberté 6"])
        liste_clients.append(["3", "SENE", "Etienne Diegane", "0123456789", "Liberté 6"])
        liste_clients.append(["3", "DIOUM", "Babacar", "0123456789", "Yoff"])

        # Création du widget TreeView
        treeview = Gtk.TreeView(model=liste_clients)

        # Création des colonnes
        id_colonne = Gtk.TreeViewColumn("ID", Gtk.CellRendererText(), text=0)
        treeview.append_column(id_colonne)

        prenom_colonne = Gtk.TreeViewColumn("Prénom", Gtk.CellRendererText(), text=1)
        treeview.append_column(prenom_colonne)

        nom_colonne = Gtk.TreeViewColumn("Nom", Gtk.CellRendererText(), text=2)
        treeview.append_column(nom_colonne)

        tel_colonne = Gtk.TreeViewColumn("Téléphone", Gtk.CellRendererText(), text=3)
        treeview.append_column(tel_colonne)

        adresse_colonne = Gtk.TreeViewColumn("Adresse", Gtk.CellRendererText(), text=4)
        treeview.append_column(adresse_colonne)

        # Ajout du widget TreeView à la fenêtre
        win.add(treeview)

        win.show_all()



        
        
    def on_liste_present_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour afficher la liste des clients présent dans l'hotel
        win = Gtk.Window(title="Liste des clients actuellement présent dans   l'hôtel")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(400, 300)

        # Création du modèle de données
        liste_clients = Gtk.ListStore(str, str, str, str, str, str, )
        # Ajouter des données de test
        liste_clients.append(["1", "SOW", " Ibrahima", "0123456789", "Dalifort", "0451", ])
        liste_clients.append(["2", "DIARRA", "Abdoullaye", "0123456789", "Liberté 6","0321" ])
        liste_clients.append(["3", "SENE", "Etienne Diegane ", "0123456789", "Liberté 6", "0554" ])
        liste_clients.append(["3", "DIOUM", "BABACAR", "0123456789", "Yoff" , "0640" ])

        # Création du widget TreeView
        treeview = Gtk.TreeView(model=liste_clients)

        # Création des colonnes
        id_colonne = Gtk.TreeViewColumn("ID", Gtk.CellRendererText(), text=0)
        treeview.append_column(id_colonne)

        prenom_colonne = Gtk.TreeViewColumn("Prénom", Gtk.CellRendererText(), text=1)
        treeview.append_column(prenom_colonne)

        nom_colonne = Gtk.TreeViewColumn("Nom", Gtk.CellRendererText(), text=2)
        treeview.append_column(nom_colonne)

        tel_colonne = Gtk.TreeViewColumn("Téléphone", Gtk.CellRendererText(), text=3)
        treeview.append_column(tel_colonne)

        adresse_colonne = Gtk.TreeViewColumn("Adresse", Gtk.CellRendererText(), text=4)
        treeview.append_column(adresse_colonne)
        
        Etage_colonne = Gtk.TreeViewColumn("Etage et numéro chambre", Gtk.CellRendererText(), text=5)
        treeview.append_column(Etage_colonne)

        
        
      

        # Ajout du widget TreeView à la fenêtre
        win.add(treeview)

        win.show_all()
        
        
    def on_liste_chambres_clicked(self, widget):
        # Ouvrir une nouvelle fenêtre pour afficher la liste des chambres
        win = Gtk.Window(title="Liste des chambres")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(400, 300)

        # Création du modèle de données
        liste_chambres = Gtk.ListStore(str, str, str, str)
        # Ajouter des données de test
        liste_chambres.append(["00", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "économique", "50.000"])
        liste_chambres.append(["01", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "économique", "50.000"])
        liste_chambres.append(["02", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "économique", "50.000" ])
        liste_chambres.append(["03", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "standing", "100.000" ])
        liste_chambres.append(["04", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15",  "standing", "100.000" ])
        liste_chambres.append(["05", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15",  "standing", "150000" ])
        liste_chambres.append(["06", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15",  "affaires", "150000" ])
        liste_chambres.append(["07", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15",  "affaires", "150000" ])
        liste_chambres.append(["08", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15",  "affaires", "150000" ])
       

        # Création du widget TreeView
        treeview = Gtk.TreeView(model=liste_chambres)

        # Création des colonnes
        Etage = Gtk.TreeViewColumn("Etage", Gtk.CellRendererText(), text=0)
        treeview.append_column(Etage)

        Chambre = Gtk.TreeViewColumn("Numéro Chambre", Gtk.CellRendererText(), text=1)
        treeview.append_column(Chambre)
        
        classe = Gtk.TreeViewColumn("Classe Chambre", Gtk.CellRendererText(), text=2)
        treeview.append_column(classe)
        
        prix = Gtk.TreeViewColumn("Prix Chambre", Gtk.CellRendererText(), text=3)
        treeview.append_column(prix)

       
        # Ajout du widget TreeView à la fenêtre
        win.add(treeview)

        win.show_all()
        
        
    def on_chambres_occupee(self, widget):
        # Ouvrir une nouvelle fenêtre pour afficher la liste des chambres
        win = Gtk.Window(title="Liste des chambres occupées")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(400, 300)

        # Création du modèle de données
        chambres_occupee = Gtk.ListStore(str, str, str)
        # Ajouter des données de test
        chambres_occupee.append(["00", "01 02 03 04  08 09 13 14 15", "occupée"])
        chambres_occupee.append(["01", "01 02 03 04  07 08 09   12 13 14 15", "occupée"])
        chambres_occupee.append(["02", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "occupée"])
        chambres_occupee.append(["03", "01 02 03 04 05 06 07 08 0 12 13 14 15", "occupée"])
        chambres_occupee.append(["04", "03 04  06 07  09 10 11   14 15", "occupée" ])
        chambres_occupee.append(["05", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "occupée" ])
        chambres_occupee.append(["06", "01 02 03 04 05 06 07 08 09 13 14 15", "occupée" ])
        chambres_occupee.append(["08", "01 02 03 0  07 08 09 10 12  14 15", "occupée" ])
       

        # Création du widget TreeView
        treeview = Gtk.TreeView(model=chambres_occupee)

        # Création des colonnes
        Etage = Gtk.TreeViewColumn("Etage", Gtk.CellRendererText(), text=0)
        treeview.append_column(Etage)

        Chambre = Gtk.TreeViewColumn("Numéro Chambre", Gtk.CellRendererText(), text=1)
        treeview.append_column(Chambre)
        
        Statut = Gtk.TreeViewColumn("Statut", Gtk.CellRendererText(), text=2)
        treeview.append_column(Statut)

       
        # Ajout du widget TreeView à la fenêtre
        win.add(treeview)

        win.show_all()
        
    
        
        
        
    def on_chambres_reservees(self, widget):
        # Ouvrir une nouvelle fenêtre pour afficher la liste des chambres
        win = Gtk.Window(title="Liste des chambres reservées")
        win.connect("destroy", Gtk.main_quit)
        win.set_default_size(400, 300)

        # Création du modèle de données
        chambres_reservees = Gtk.ListStore(str, str, str)
        # Ajouter des données de test
        chambres_reservees.append(["00", "01 02 03 04  08 09 13 14 15", "reservées"])
        chambres_reservees.append(["01", "01 02 03 04  07 08 09   12 13 14 15", "reservées"])
        chambres_reservees.append(["02", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "reservées"])
        chambres_reservees.append(["03", "01 02 03 04 05 06 07 08 0 12 13 14 15", "reservées"])
        chambres_reservees.append(["04", "03 04  06 07  09 10 11   14 15", "reservées" ])
        chambres_reservees.append(["05", "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15", "reservées" ])
        chambres_reservees.append(["06", "01 02 03 04 05 06 07 08 09 13 14 15", "reservées" ])
        chambres_reservees.append(["08", "01 02 03 0  07 08 09 10 12  14 15", "reservées" ])
       

        # Création du widget TreeView
        treeview = Gtk.TreeView(model=chambres_reservees)

        # Création des colonnes
        Etage = Gtk.TreeViewColumn("Etage", Gtk.CellRendererText(), text=0)
        treeview.append_column(Etage)

        Chambre = Gtk.TreeViewColumn("Numéro Chambre", Gtk.CellRendererText(), text=1)
        treeview.append_column(Chambre)
        
        Statut = Gtk.TreeViewColumn("Statut", Gtk.CellRendererText(), text=2)
        treeview.append_column(Statut)

       
        # Ajout du widget TreeView à la fenêtre
        win.add(treeview)

        win.show_all()





    def on_statistiques_clicked(data, annee=None, nb_clients=False, chiffre_affaire=False, diagramme=False):
       
       
        
        if annee:
            data = {k: v for k, v in data.items() if v['annee'] == annee}
            
        if nb_clients:
            nb_clients_par_annee = {}
            for k, v in data.items():
                if v['annee'] in nb_clients_par_annee:
                    nb_clients_par_annee[v['annee']] += 1
                else:
                    nb_clients_par_annee[v['annee']] = 1
            print("Nombre de clients par année : ")
            #for k, v in nb_clients_par_annee.items():
             #   print(f"{k} : {v}")
            
        if chiffre_affaire:
            chiffre_affaire_par_annee = {}
            for k, v in data.items():
                if v['annee'] in chiffre_affaire_par_annee:
                    chiffre_affaire_par_annee[v['annee']] += v['vente']
                else:
                    chiffre_affaire_par_annee[v['annee']] = v['vente']
            print("Chiffre d'affaire par année : ")
           # for k, v in chiffre_affaire_par_annee.items():
           #     print(f"{k} : {v}")
                
   



      
       

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
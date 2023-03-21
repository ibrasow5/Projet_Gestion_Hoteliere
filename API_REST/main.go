package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

const port1 = ":8080"

type Client struct {
	Id_client        int    `json:"id_client"`
	Prenom_client    string `json:"prenom_client"`
	Nom_client       string `json:"nom_client"`
	Telephone_client string `json:"telephone_client"`
}

type Chambre struct {
	Num           int    `json:"num"`
	Disponibilite string `json:"disponibilite"`
	Niveau        int    `json:"niveau"`
}

type Reservation struct {
	Id_reserv   int    `json:"id_reserv"`
	Date_reserv string `json:"date_reserv"`
	Date_entree string `json:"date_entree"`
	Date_sortie string `json:"date_sortie"`
	Nuitee      int    `json:"nuitee"`
}

type Hotel struct {
	Nom          string `json:"nom_hotel"`
	Nbre_niveau  int    `json:"nbre_niveau"`
	Nbre_chambre int    `json:"nbre_chambre"`
	Adresse      string `json:"adresse"`
	Tel          string `json:"tel"`
	Nbre_etoiles string `json:"nbre_etoiles"`
}

type Facture struct {
	Id_facture     int     `json:"id_facture"`
	Tarif_chambre  float32 `json:"tarif_chambre"`
	Tarif_services float32 `json:"tarif_services"`
	Total          float32 `json:"total"`
}

type Service struct {
	Nom   string  `json:"nom_service"`
	Tarif float32 `json:"tarif_service"`
}

type Categorie struct {
	Classe     string `json:"classe"`
	Type_tarif string `json:"type_tarif"`
}

func main() {
	// les données de notre serveur SQL
	server := "localhost"
	port := 6303
	user := "playgrounduser"
	password := "playgroundpassword"
	database := "hotellerie"

	// Créez une chaîne de connexion
	connString := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s", user, password, server, port, database)

	// Ouvrez une connexion
	db, err := sql.Open("mysql", connString)
	if err != nil {
		fmt.Println("Echec connexion")
		panic(err.Error())
	}

	// Vérifiez que la connexion est bien établie
	err = db.Ping()
	if err != nil {
		fmt.Println("Echec connexion")
		panic(err.Error())
	}

	// Fermez la connexion lorsque vous avez terminé
	defer db.Close()

	// Afficher un message de connexion réussie
	log.Println("Bien connecté - la connexion avec la base de données est correcte.")

	// Créez un gestionnaire de requêtes HTTP
	http.HandleFunc("/clients", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "GET" {
			// Exécutez une requête SQL pour récupérer tous les clients
			rows, err := db.Query("SELECT * FROM client")
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			defer rows.Close()

			// Parcourez les résultats de la requête et créez une liste de clients
			clients := []Client{}
			for rows.Next() {
				var client Client
				err := rows.Scan(&client.Id_client, &client.Prenom_client, &client.Nom_client, &client.Telephone_client)
				if err != nil {
					http.Error(w, err.Error(), http.StatusInternalServerError)
					return
				}
				clients = append(clients, client)
			}
			if err := rows.Err(); err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Créez une réponse JSON avec la liste des clients
			json.NewEncoder(w).Encode(clients)
		} else if r.Method == "POST" {
			// Récupérez le corps de la requête JSON
			var client Client
			err := json.NewDecoder(r.Body).Decode(&client)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Exécutez une requête SQL pour insérer le nouveau client dans la base de données
			result, err := db.Exec("INSERT INTO client(Id_client, Prenom_client, Nom_client, Telephone_client) VALUES(?, ?, ?, ?)", client.Id_client, client.Prenom_client, client.Nom_client, client.Telephone_client)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Récupérez l'ID du nouveau client inséré dans la base de données
			id, err := result.LastInsertId()
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Renvoyez une réponse JSON avec l'ID du nouveau client
			response := map[string]int64{"id_client": id}
			json.NewEncoder(w).Encode(response)
		} else if r.Method == "PUT" {
			// Récupérez l'ID du client à mettre à jour à partir de la requête URL
			Id_client := r.URL.Path[len("/clients/"):]

			// Récupérez le corps de la requête JSON
			var updatedClient Client
			err := json.NewDecoder(r.Body).Decode(&updatedClient)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Mettez à jour le client dans la base de données
			result, err := db.Exec("UPDATE client SET Prenom_client = ?, Nom_client = ?, Telephone_client = ? WHERE Id_client = ?", updatedClient.Prenom_client, updatedClient.Nom_client, updatedClient.Telephone_client, Id_client)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Renvoyez une réponse JSON avec le nombre de lignes modifiées
			rowsAffected, err := result.RowsAffected()
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			response := map[string]int64{"rows_affected": rowsAffected}
			json.NewEncoder(w).Encode(response)
		}
	})
	http.HandleFunc("/clients/{Id_client}", func(w http.ResponseWriter, r *http.Request) {
		// Récupérez l'identifiant de la réservation à partir des variables de chemin
		vars := mux.Vars(r)
		id, err := strconv.Atoi(vars["Id_client"])
		if err != nil {
			http.Error(w, "Invalid Client ID", http.StatusBadRequest)
			return
		}

		// Récupérez la réservation à partir de la base de données
		rows, err := db.Query("SELECT * FROM client WHERE ID_client = ?", id)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		defer rows.Close()

		// Vérifiez que la réservation a été trouvée
		if !rows.Next() {
			http.Error(w, "Client not found", http.StatusNotFound)
			return
		}

		// Parcourez les résultats de la requête et créez une instance de réservation
		var client Client
		err = rows.Scan(&client.Id_client, &client.Prenom_client, &client.Nom_client, &client.Telephone_client)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		// Renvoyer la réservation sous forme de réponse JSON
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(client)
	})

	// Méthode GET pour récupérer toutes les réservations
	http.HandleFunc("/reservations", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "GET" {
			// Récupérez toutes les réservations de la base de données
			rows, err := db.Query("SELECT Id_reserv, Date_reserv, Date_entree, Date_sortie, Nuitee FROM reservation")
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			defer rows.Close()

			// Parcourez les résultats de la requête et créez une liste de réservations
			reservations := []Reservation{}
			for rows.Next() {
				var reservation Reservation
				err := rows.Scan(&reservation.Id_reserv, &reservation.Date_reserv, &reservation.Date_entree, &reservation.Date_sortie, &reservation.Nuitee)
				if err != nil {
					http.Error(w, err.Error(), http.StatusInternalServerError)
					return
				}
				reservations = append(reservations, reservation)
			}
			if err := rows.Err(); err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Créez une réponse JSON avec la liste des réservations
			json.NewEncoder(w).Encode(reservations)
		} else if r.Method == "POST" {
			// Analyser le corps de la requête JSON dans une struct réservation
			var reservation Reservation
			err := json.NewDecoder(r.Body).Decode(&reservation)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Exécutez une requête SQL pour insérer la nouvelle reservation dans la base de données
			stmt, err := db.Prepare("INSERT INTO reservation(Id_reserv, Date_reserv, Date_entree, Date_sortie, Nuitee) VALUES(?, ?, ?, ?, ?)")
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			defer stmt.Close()

			// Renvoyer la réservation ajoutée avec un code de statut HTTP 201 Created
			w.WriteHeader(http.StatusCreated)
			json.NewEncoder(w).Encode(reservation)

		} else if r.Method == "PUT" {
			// Récupérez l'ID de la réservation à mettre à jour à partir de la requête URL
			vars := mux.Vars(r)
			reservationID, err := strconv.Atoi(vars["Id_reserv"])
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Decodez le corps de la requête en une variable de type Reservation
			var updatedReservation Reservation
			err = json.NewDecoder(r.Body).Decode(&updatedReservation)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Exécutez une requête SQL pour mettre à jour la reservation dans la base de données
			result, err := db.Exec("UPDATE reservation SET Date_reserv = ?, Date_entree = ?, Date_sortie = ?, Nuitee = ? WHERE Id_reserv = ?", updatedReservation.Date_reserv, updatedReservation.Date_entree, updatedReservation.Date_sortie, updatedReservation.Nuitee, reservationID)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Vérifiez que la réservation a bien été mise à jour
			rowsAffected, err := result.RowsAffected()
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			if rowsAffected == 0 {
				http.Error(w, "Réservation introuvable", http.StatusNotFound)
				return
			}

			// Encodez la réponse en JSON et envoyez-la
			response := map[string]int{"Id_reserv": reservationID}
			json.NewEncoder(w).Encode(response)
		}
	})

	http.HandleFunc("/reservations/{Id_reserv}", func(w http.ResponseWriter, r *http.Request) {
		// Récupérez l'identifiant de la réservation à partir des variables de chemin
		vars := mux.Vars(r)
		id_reserv, err := strconv.Atoi(vars["Id_reserv"])
		if err != nil {
			http.Error(w, "Invalid reservation ID", http.StatusBadRequest)
			return
		}

		// Récupérez la réservation à partir de la base de données
		rows, err := db.Query("SELECT * FROM reservation WHERE ID_reserv = ?", id_reserv)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		defer rows.Close()

		// Vérifiez que la réservation a été trouvée
		if !rows.Next() {
			http.Error(w, "Reservation not found", http.StatusNotFound)
			return
		}

		// Parcourez les résultats de la requête et créez une instance de réservation
		var reservation Reservation
		err = rows.Scan(&reservation.Id_reserv, &reservation.Date_reserv, &reservation.Date_entree, &reservation.Date_sortie, &reservation.Nuitee)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		// Renvoyer la réservation sous forme de réponse JSON
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(reservation)
	})

	// Gestion de l'API REST pour les chambres
	// Gestion de l'API REST pour les chambres
	http.HandleFunc("/chambres", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "GET" {
			// Exécutez une requête SQL pour récupérer tous les chambres
			rows, err := db.Query("SELECT * FROM chambre")
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			defer rows.Close()

			// Parcourez les résultats de la requête et créez une liste de chambres
			chambres := []Chambre{}
			for rows.Next() {
				var chambre Chambre
				err := rows.Scan(&chambre.Num, &chambre.Disponibilite, &chambre.Niveau)
				if err != nil {
					http.Error(w, err.Error(), http.StatusInternalServerError)
					return
				}
				chambres = append(chambres, chambre)
			}
			if err := rows.Err(); err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Créez une réponse JSON avec la liste des chambres
			json.NewEncoder(w).Encode(chambres)
		} else if r.Method == "POST" {
			// Récupérez le corps de la requête JSON
			var newChambre Chambre
			err := json.NewDecoder(r.Body).Decode(&newChambre)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Insérez la nouvelle chambre dans la base de données
			result, err := db.Exec("INSERT INTO chambre (Num, Disponibilité, Niveau) VALUES (?, ?, ?)", newChambre.Num, newChambre.Disponibilite, newChambre.Niveau)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Récupérez l'ID de la nouvelle chambre insérée
			newID, err := result.LastInsertId()
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Renvoyez une réponse JSON avec l'ID de la nouvelle chambre
			response := map[string]int64{"num_chambre": newID}
			json.NewEncoder(w).Encode(response)

		} else if r.Method == "PUT" {
			// Decodez le corps de la requête en une variable de type chambre
			var chambre Chambre
			err := json.NewDecoder(r.Body).Decode(&chambre)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Exécutez une requête SQL pour mettre à jour le chambre dans la base de données
			stmt, err := db.Prepare("UPDATE Disponibilite = ?, Niveau = ? WHERE Num = ?")
			if err != nil {
				log.Fatal(err)
			}
			defer stmt.Close()

			_, err = stmt.Exec(chambre.Disponibilite, chambre.Niveau, chambre.Num)
			if err != nil {
				log.Fatal(err)
			}

			// Encodez la réponse en JSON et envoyez-la
			w.Header().Set("Content-Type", "application/json")
			err = json.NewEncoder(w).Encode(map[string]string{"message": "chambre mise à jour avec succès"})
			if err != nil {
				log.Fatal(err)
			}

		} else if r.Method == "DELETE" {
			// Récupérez l'ID du chambre à supprimer depuis les paramètres de requête
			idStr := r.URL.Query().Get("id")
			if idStr == "" {
				http.Error(w, "Paramètre ID manquant", http.StatusBadRequest)
				return
			}
			Num, err := strconv.Atoi(idStr)
			if err != nil {
				http.Error(w, "Paramètre ID invalide", http.StatusBadRequest)
				return
			}

			// Exécutez une requête SQL pour supprimer le chambre de la base de données
			result, err := db.Exec("DELETE FROM chambre WHERE Num = ?", Num)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Vérifier si la suppression a affecté une ligne
			rowsAffected, err := result.RowsAffected()
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			if rowsAffected == 0 {
				http.Error(w, "Chambre not found", http.StatusNotFound)
				return
			}

			// Envoyer une réponse de succès
			w.WriteHeader(http.StatusNoContent)
		}
	})

	// Créez un gestionnaire de requêtes HTTP
	http.HandleFunc("/hotel", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == "GET" {
			// Exécutez une requête SQL pour récupérer tous les hotel
			rows, err := db.Query("SELECT * FROM hotel")
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			defer rows.Close()

			// Parcourez les résultats de la requête et créez une liste de l'hotel
			hotels := []Hotel{}
			for rows.Next() {
				var hotel Hotel
				err := rows.Scan(&hotel.Nom, &hotel.Nbre_niveau, &hotel.Nbre_chambre, &hotel.Adresse, &hotel.Tel, &hotel.Nbre_etoiles)
				if err != nil {
					http.Error(w, err.Error(), http.StatusInternalServerError)
					return
				}
				hotels = append(hotels, hotel)
			}
			if err := rows.Err(); err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Créez une réponse JSON avec la liste des hotels
			json.NewEncoder(w).Encode(hotels)
		} else if r.Method == "POST" {
			// Récupérez le corps de la requête JSON
			var hotel Hotel
			err := json.NewDecoder(r.Body).Decode(&hotel)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			// Exécutez une requête SQL pour insérer le nouveau hotel dans la base de données
			result, err := db.Exec("INSERT INTO hotel(Nom, Nbre_niveau, Nbre_chambre, Adresse, Tel, Nbre_etoiles) VALUES(?, ?, ?, ?, ?, ?)", hotel.Nom, hotel.Nbre_niveau, hotel.Nbre_chambre, hotel.Adresse, hotel.Tel, hotel.Nbre_etoiles)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Récupérez l'ID du nouveau hotel inséré dans la base de données
			id, err := result.LastInsertId()
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Renvoyez une réponse JSON avec l'ID du nouveau hotel
			response := map[string]int64{"id_hotel": id}
			json.NewEncoder(w).Encode(response)

		} else if r.Method == "DELETE" {
			// Récupérez l'ID de l'hotel à supprimer à partir de la requête URL
			Id_hotel := r.URL.Path[len("/hotel/"):]

			// Supprimez le'otel dans la base de données
			result, err := db.Exec("DELETE FROM hotel WHERE Id_hotel = ?", Id_hotel)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			// Renvoyez une réponse JSON avec le nombre de lignes supprimées
			rowsAffected, err := result.RowsAffected()
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			response := map[string]int64{"rows_affected": rowsAffected}
			json.NewEncoder(w).Encode(response)
		}
	})

	// Lancez le serveur HTTP
	fmt.Println("(http:localhost//:8080) - Server started on port", port1)
	http.ListenAndServe(port1, nil)

}

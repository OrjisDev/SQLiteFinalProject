#import des bibliothèques
import requests
import json

#Url du serveur
server_url = "http://localhost:8000/"

#Boucle d'execution du programme
while True:
    request_type = -1
    #Au cas ou l'utilisateur se trompe la condition se répète jusqu'a ce que l'entrtée utilisateur soit valide
    while request_type == -1 or request_type > 4:
        #Affiche graphiquement le texte inclu dans la fonction input(), demande une entrée, associe l'entrée à la variable request_type
        request_type = int(
            input(
                "Vous avez 4 choix dans l'utilisation de l'application (tapez le nombre qui correspond) :"
                + "\n 1 : Donner un nom d'artiste pour récupérer la liste des artistes comprenant le nom donné"
                + "\n 2 : Donner un identifiant d'artiste pour afficher les noms d'albums correspondants"
                + "\n 3 : Donner un identifiant d'album pour afficher les pistes correspondantes"
                + "\n 4 : Sortir de l'application \n"
            )
        )
        #Dans le cas ou request_type = 1 on demande le nom d'artiste 
        if request_type == 1:
            #Demande les arguments à passer dans la requête
            argument = input("Saisis le nom d'artiste : ")
            #Effectue la requête au serveur et attribue le retour à la variable response
            response = requests.get(f'{server_url}artists/{argument}')
            #Récupération du corps de la réponse du serveur en json 
            body = response.json()
            bodylenght = len(body)
            #Boucle qui renvoie pour chaque entrée dans "body" la valeur associée à la clef 'name'
            if bodylenght != 0:
                print("Voici les artistes correspondant à votre recherche :")
                for i in range(bodylenght):
                    print(body[i]['name'])
            #Si 'body' n'as pas de contenu
            else:
                print("Aucun artiste n'as été trouvé")
            input("Entrée pour continuer le programme : ")
        #Répetition du 1
        if request_type == 2:
            argument = input("Saisis l'id d'artiste : ")
            response = requests.get(f'{server_url}albums/{argument}')
            body = response.json()
            bodylenght = len(body)
            if bodylenght != 0:
                print("Voici les albums correspondant à votre recherche :")
                for i in range(bodylenght):
                    print(body[i]['title'])
            else:
                print("Aucun artiste n'as été trouvé")
            input("Entrée pour continuer le programme : ")
        #Répetition du 1
        if request_type == 3:
            argument = input("Saisis l'id d'album : ")
            response = requests.get(f'http://localhost:8000/tracks/'+argument)
            body = response.json()
            bodylenght = len(body)
            if bodylenght != 0:
                print("Voici les pistes correspondant à votre recherche :")
                for i in range(bodylenght):
                    print(body[i]['name'])
            else:
                print("Aucune piste n'as été trouvée")
            input("Entrée pour continuer le programme : ")
        if request_type == 4:
            exit()

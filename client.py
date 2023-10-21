import requests

server_url = "localhost:8000"

while True:
    request_type = -1
    while request_type == -1 or request_type > 4:
        request_type = int(
            input(
                "Vous avez 4 choix dans l'utilisation de l'application (tapez le nombre qui correspond) :"
                + "\n 1 : Donner un nom d'artiste pour récupérer la liste des artistes comprenant le nom donné"
                + "\n 2 : Donner un identifiant d'artiste pour afficher les noms d'albums correspondants"
                + "\n 3 : Donner un identifiant d'album pour afficher les pistes correspondantes"
                + "\n 4 : Sortir de l'application \n"
            )
        )
    if request_type == 1:
        argument = input("Saisis le nom d'artiste : ")
        requete = requests.get(server_url + f"/artists/{argument}")

    if request_type == 4:
        exit()
    else:
        print("Choix absent de la liste")

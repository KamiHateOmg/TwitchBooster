# Affiche le message de demande
print("Que veux-tu remplacer ?")

# Affiche les options
print("1. Erreur")
print("2. Shutdwon message")
print("3. Voix")
print("4. Webhook du Stealer.. SOON")

# Demande à l'utilisateur de choisir une option
choix = input("Choisis une option : ")

# Vérifie l'option choisie et effectue l'action appropriée
if choix == "1":
    print("Tu as choisi l'option 1.")
    remplacement1 = input("Par quoi veux-tu remplacer l'erreur ?")

    # Ouvre le fichier hello.vbs en mode lecture
    with open("virus\msg.vbs", "r") as fichier:
        lignes = fichier.readlines()

    ligne_modifiee1 = lignes[0].replace("alors c'est comment d'etre un fils de pute ?", remplacement1)

    lignes[0] = ligne_modifiee1

    # Écrit les lignes modifiées dans le fichier hello.vbs
    with open("virus\msg.vbs", "w") as fichier:
        fichier.writelines(lignes)

    print("Le fichier msg.vbs a été modifié avec succès.")

    remplacement2 = input("Par quoi veux-tu remplacer le titre de l'erreur ?")

    # Modifie la ligne 35 avec le remplacement2 pour "1234"
    ligne_modifiee2 = lignes[0].replace("FUCKED BY KAMI", remplacement2)

    # Remplace à nouveau la ligne dans la liste des lignes
    lignes[0] = ligne_modifiee2

    # Écrit les lignes modifiées dans le fichier hello.vbs
    with open("virus\msg.vbs", "w") as fichier:
        fichier.writelines(lignes)

    print("Le fichier msg.vbs a été modifié avec succès.")

elif choix == "2":
    print("Tu as choisi l'option 2.")
    remplacement3 = input("Par quoi veux-tu remplacer le message du shutdown?")

    # Ouvre le fichier hello.vbs en mode lecture
    with open("virus\hidden.bat", "r") as fichier:
        lignes = fichier.readlines()

    ligne_modifiee3 = lignes[33].replace("Dans 5 minutes tu n'as plus de PC fils de pute :)", remplacement3)

    lignes[33] = ligne_modifiee3

    # Écrit les lignes modifiées dans le fichier hello.vbs
    with open("virus\hidden.bat", "w") as fichier:
        fichier.writelines(lignes)

    print("Le fichier hidden.bat a été modifié avec succès.")
elif choix == "3":
    print("Tu as choisi l'option 3.")
    remplacement4 = input("Par quoi veux-tu remplacer la voix ?")

    # Ouvre le fichier hello.vbs en mode lecture
    with open(r'virus\voice.vbs', "r") as fichier:
        lignes = fichier.readlines()

    ligne_modifiee4 = lignes[2].replace("Coucou toi, je t'ai bien niquer ta race ! Ton pc est mort dans 5 minutes. Amuse toi bien a le reparer fils de pute. Regarde bien ton pc mourrir petite merde", remplacement4)

    lignes[2] = ligne_modifiee4

    # Écrit les lignes modifiées dans le fichier hello.vbs
    with open(r'virus\voice.vbs', "w") as fichier:
        fichier.writelines(lignes)

    print("Le fichier voice.vbs a été modifié avec succès.")
elif choix == "4":
    print("Bientot tkt")
else:
    print("Option invalide.")

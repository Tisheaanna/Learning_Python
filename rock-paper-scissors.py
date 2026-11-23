import random 

#Scores starts at 0
Score_joueur =  0
score_ordi = 0

while score_ordi <3 and score_ordi <3: #While the score is under 3, game keep running

    choix_possible = ["pierre","feuille", "ciseaux"] 

    choix_ordi = random.choice(choix_possible) #Choose 'choix possible'
    print("-------CHOIX ORDI--------")

    choix_utilisateur = input("Choisi entre pierre, feuille et ciseaux")
    print("vous avez choisi = ", choix_utilisateur)

    if choix_utilisateur == choix_ordi:
        print("égalité!")
    elif (choix_utilisateur == "pierre" and choix_ordi == "ciseaux") or \
    (choix_utilisateur=="ciseaux" and choix_ordi== "feuille") or\
    (choix_utilisateur=="feuille" and choix_ordi== "pierre"):
     print("you win ! +1 pts")
     Score_joueur = Score_joueur + 1
     

   

    else :
        print("l'ordi gagne la manche")
        score_ordi = score_ordi + 1 

    print ("-----------")
    print (" Toi : ", Score_joueur, "ordi :" , score_ordi)
    print("------------")

if Score_joueur == 3 :
    print("_________________________")
    print("BRAVO ! ")
    print("__________________________")
else :
    print("___________________________")
    print("You loose !")
    print("_______________________________")




    







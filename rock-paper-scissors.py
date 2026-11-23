import random 

#Scores starts at 0
User_Score =  0
Computer_Score = 0

while User_Score <3 and Computer_Score <3: #While the score is under 3, game keep running

    Possible_Choice = ["rock","paper", "scissors"] 

    Computer_Choice = random.choice(Possible_Choice) #Choose
    print("-------Computer choose --------")

    User_choice = input("Choose between rock, paper and scissors")
    print("You choose = ", User_choice)

    if User_choice == Computer_Choice:
        print("equality!")
    elif (User_choice == "rock" and Computer_Choice == "scissors") or \
    (User_choice=="scissors" and Computer_Choice== "paper") or\
    (User_choice=="paper" and Computer_Choice== "rock"):
     print("you win ! +1 pts")
     User_Score = User_Score + 1
     

   

    else :
        print("Computer wins")
        Computer_Score = Computer_Score + 1 

    print ("-----------")
    print (" You : ", User_Score, "Computer :" , Computer_Score)
    print("------------")

if User_Score == 3 :
    print("_________________________")
    print("GG ! ")
    print("__________________________")
else :
    print("___________________________")
    print("You loose !")
    print("_______________________________")




    







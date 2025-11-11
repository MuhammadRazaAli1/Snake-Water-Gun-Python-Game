import random 

for score in range(1, 1111):
 user_dict = {"w" : "water" , "g" : "gun" , "s" : "snake"}
 computer_choose = random.choice(["w" , "g" , "s"])
 player = input("Enter your choice: ")
 print(f"You choose {user_dict[player]}\nComputer choose {user_dict[computer_choose]}")

 if computer_choose == player:
    print(f"It's draw!")
 else:
    if (computer_choose == "w") and (player == "g"):
        print(f"You loss!")
    elif (computer_choose == "w") and (player == "s"):
        print(f"You win!")
    elif (computer_choose == "g") and (player == "w"):
        print(f"You win!")
    elif (computer_choose == "g") and (player == "s"):
        print(f"You loss!")
    elif (computer_choose == "s") and (player == "w"):
        print(f"You loss!")
    elif (computer_choose == "s") and (player == "g"):
        print(f"You win!")
    else: 
        print(f"Something went wrong!")

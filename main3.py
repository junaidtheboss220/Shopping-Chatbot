Groceries = []
exit = False
print ("Hello, welcome to the store how can I help you today dear Sir/Madam\n\n")
name = input(f"Kindly enter your name!  ")
print (f"\nWelcome {name},") 
while exit == False:
    choice = int(input("Choose the department you wish to shop in\n(1.Groceries  2.Frozen Food   3.Utensils   4.Clothes   5.Exit.)\n(Type the number!)\n"))
    if choice == 1:
        print ("You chose to go to the groceries!\n\n")
        grocerieType = int(input("Which Groceries Do you want? \n 1.Milk\n 2.Cereal\n 3.Bread\n 4.Meat\n"))
        if grocerieType == 1:
            Groceries.append ("Milk")
        elif grocerieType == 2:
            Groceries.append ("Cereal")
        elif grocerieType == 3:
            Groceries.append ("Bread")
        elif grocerieType == 4:
            Groceries.append ("Meat")
    elif choice == 2:
        print ("You chose to go to the Frozen Food!\n\n")
        FrozenFood = int(input("Which type of Frozen Food do you want?\n1.Ice Cream\n 2.Popsicles\n 3.Frozen Fruit\n 4.Premade frozen food\n"))
        if FrozenFood == 1:
            Groceries.append ("Ice cream")
        elif FrozenFood == 2:
            Groceries.append ("Popsicle")
        elif FrozenFood == 3:
            Groceries.append ("Frozen Fruit")
        elif FrozenFood == 4:
            Groceries.append ("Pre-Made Frozen Food")
    elif choice == 3:
        print ("You chose to go to the Utensils!\n\n")
        Utensil = int(input("What utensil do you want?\n 1.Forks \n 2.Knifes \n 3.Plates\n 4.Cups\n\n"))
        if Utensil == 1:
            Groceries.append ("Forks")
        elif Utensil == 2:
            Groceries.append ("Knifes")
        elif Utensil == 3:
            Groceries.append ("Plates")
        elif Utensil == 4:
            Groceries.append ("Cups")
    elif choice == 4:
        print ("You chose to go to the clothes section!\n\n")
        clothes = int(input("What clothes do you want?\n 1.Shirts \n 2.Shorts \n 3.Trousers \n 4.Shoes"))
        if clothes == 1:
            Groceries.append ("Shirt")
        elif clothes == 2:
            Groceries.append ("Shorts")
        elif clothes == 3:
            Groceries.append ("Trousers")
        elif clothes == 4:
            Groceries.append ("Shoes")
    elif choice == 5:
        exit = True
    else:
        print ("Invalid number!")
    print (f" Your Groceries:{Groceries}")
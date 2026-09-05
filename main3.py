Groceries = []
FrozenFood = []
Utensils = []
Clothes = []
Bakery = []

print("Hello, welcome to the store! How can I help you today?\n")

name = input("Kindly enter your name! ")

print(f"\nWelcome {name}!")

# Ask the user for their budget
budget = float(input("What is your budget today? £"))

print(f"\nYour budget is £{budget:.2f}. Let's start shopping!")

while True:

    choice = int(input(
        "\nChoose the department you wish to shop in:\n"
        "1. Groceries\n"
        "2. Frozen Food\n"
        "3. Utensils\n"
        "4. Clothes\n"
        "5. Bakery\n"
        "6. Exit\n"
        "Type the number: "
    ))

    if choice == 1:
        print("\nYou chose the Groceries department!")

        groceryType = int(input(
            "\nWhich groceries do you want?\n"
            "1. Milk\n"
            "2. Cereal\n"
            "3. Bread\n"
            "4. Meat\n"
            "Type the number: "
        ))

        if groceryType == 1:
            Groceries.append("Milk")
        elif groceryType == 2:
            Groceries.append("Cereal")
        elif groceryType == 3:
            Groceries.append("Bread")
        elif groceryType == 4:
            Groceries.append("Meat")
        else:
            print("Invalid number!")

    elif choice == 2:
        print("\nYou chose the Frozen Food department!")

        frozenType = int(input(
            "\nWhich frozen food do you want?\n"
            "1. Ice Cream\n"
            "2. Popsicles\n"
            "3. Frozen Fruit\n"
            "4. Pre-made Frozen Food\n"
            "Type the number: "
        ))

        if frozenType == 1:
            FrozenFood.append("Ice Cream")
        elif frozenType == 2:
            FrozenFood.append("Popsicles")
        elif frozenType == 3:
            FrozenFood.append("Frozen Fruit")
        elif frozenType == 4:
            FrozenFood.append("Pre-made Frozen Food")
        else:
            print("Invalid number!")

    elif choice == 3:
        print("\nYou chose the Utensils department!")

        utensilType = int(input(
            "\nWhat utensil do you want?\n"
            "1. Forks\n"
            "2. Knives\n"
            "3. Plates\n"
            "4. Cups\n"
            "Type the number: "
        ))

        if utensilType == 1:
            Utensils.append("Forks")
        elif utensilType == 2:
            Utensils.append("Knives")
        elif utensilType == 3:
            Utensils.append("Plates")
        elif utensilType == 4:
            Utensils.append("Cups")
        else:
            print("Invalid number!")

    elif choice == 4:
        print("\nYou chose the Clothes department!")

        clothesType = int(input(
            "\nWhat clothes do you want?\n"
            "1. Shirts\n"
            "2. Shorts\n"
            "3. Trousers\n"
            "4. Shoes\n"
            "Type the number: "
        ))

        if clothesType == 1:
            Clothes.append("Shirts")
        elif clothesType == 2:
            Clothes.append("Shorts")
        elif clothesType == 3:
            Clothes.append("Trousers")
        elif clothesType == 4:
            Clothes.append("Shoes")
        else:
            print("Invalid number!")

    elif choice == 5:
        print("\nYou chose the Bakery department!")

        bakeryType = int(input(
            "\nWhat bakery item do you want?\n"
            "1. Croissant\n"
            "2. Muffin\n"
            "3. Donut\n"
            "4. Cake\n"
            "Type the number: "
        ))

        if bakeryType == 1:
            Bakery.append("Croissant")
        elif bakeryType == 2:
            Bakery.append("Muffin")
        elif bakeryType == 3:
            Bakery.append("Donut")
        elif bakeryType == 4:
            Bakery.append("Cake")
        else:
            print("Invalid number!")

    elif choice == 6:
        print("\nThank you for shopping,", name + "!")
        print("Here is your shopping list:")

        print("Groceries:", Groceries)
        print("Frozen Food:", FrozenFood)
        print("Utensils:", Utensils)
        print("Clothes:", Clothes)
        print("Bakery:", Bakery)

        print(f"\nYou started with a budget of £{budget:.2f}.")
        
        break

    else:
        print("Invalid number! Please choose a department from 1-6.")


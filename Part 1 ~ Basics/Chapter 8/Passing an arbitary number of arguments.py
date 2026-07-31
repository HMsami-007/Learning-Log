def MakePizza(*Toppings):
    print("\nMaking a pizza with the following toppings:")
    for Topping in Toppings:
        print("- "+ Topping)

MakePizza('Pepperoni')
MakePizza('Mushrooms','Green Peppers','Extra Cheese')
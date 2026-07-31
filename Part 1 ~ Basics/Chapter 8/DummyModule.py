def MakePizza(Size,*Toppings):
    print(f"Making a {str(Size)}-inch pizza with the following toppings:")
    for Topping in Toppings:
        print(f"- {Topping}")
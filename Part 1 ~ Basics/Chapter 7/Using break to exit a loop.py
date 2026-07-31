Prompt="\nPlease enter a name of a city you would like to vist:"
while True:
    City=input(Prompt)
    if City=="Quit":
        break
    else:
        print(f"I would love to visit {City}")
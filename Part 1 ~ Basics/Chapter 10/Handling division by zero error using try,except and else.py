print("Give me two numbers, and I'll divide them.")
print("Enter q to quit.")
while True:
    FirstNum=input("Enter the first number:")
    if FirstNum=="q":
        break
    SecondNum=input("Enter the second number:")
    if SecondNum=="q":
        break
    try:
        Answer=int(FirstNum)/int(SecondNum)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:               ##IF TRY IS SUCCESSFUL ELSE PART IS EXECUTED OR ELSE EXCEPT PART IS EXECUTED
        print(Answer)
        
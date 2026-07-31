CurrentNumber=0
while CurrentNumber<10:
    CurrentNumber+=1
    if CurrentNumber%2==0:
        continue          #Continue means The continue keyword in Python skips the remaining code inside the current loop iteration and immediately moves the program control to the next iteration, i.e the beginning of the loop. It works within both for and while loops. Instead of breaking out of the loop completely, it simply skips ahead.
    print(CurrentNumber)
Prompt="\nTell me something, and I will repeat it back to you."
Prompt+="\nEnter 'quit' to end the program."
Message=""
while Message !="quit":
    Message=input(Prompt)
    if Message!='quit':
        print(Message)
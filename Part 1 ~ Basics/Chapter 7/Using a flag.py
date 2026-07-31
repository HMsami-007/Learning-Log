Prompt="Tell me something, and I will repeat it back to you."
Active=True
while Active:
    Message=input(Prompt)
    if Message=='Quit':
        Active=False
    else:
        print(Message)
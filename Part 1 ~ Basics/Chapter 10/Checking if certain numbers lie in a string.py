Filename="SampleText.txt"
with open(Filename) as File:
    Lines=File.readlines()

PiString=""
for Line in Lines:
    PiString+=Line.rstrip()

print(PiString)
print(len(PiString))

PiString=""
for Line in Lines:
    PiString+=Line.strip()

print(PiString)
print(len(PiString))
print(PiString[:5]+"......") 

Birthday=input("Enter your birthday in the format,mmddyy:")
if Birthday in PiString:
    print("Your birthday appears in the digits of pi")
else:
    print("Your birthday does not appear in the digits of pi")


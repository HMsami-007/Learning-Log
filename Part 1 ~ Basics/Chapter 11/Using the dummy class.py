from DummyClass1 import AnonymousSurvey
Question="What language did you first learn to speak?"
MySurvey=AnonymousSurvey(Question)
MySurvey.ShowQuestion()
print("Enter 'Quit' to quit anytim.")
while True:
    Response=input("Langauge:")
    if Response=="Quit":
        break
    MySurvey.StoreResponse(Response)
print("\nThank you to everyone who participated in the survey:")
MySurvey.ShowResults()
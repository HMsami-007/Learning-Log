class AnonymousSurvey():
    def __init__(self,Question):
        self.Question=Question
        self.Responses=[]

    def ShowQuestion(self):
        print(self.Question)
    
    def StoreResponse(self,Response):
        self.Responses.append(Response)

    def ShowResults(self):
        print("Survey Results:")
        for Response in self.Responses:
            print("-"+ Response)
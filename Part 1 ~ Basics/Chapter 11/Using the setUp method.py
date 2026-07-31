import unittest
from DummyClass1 import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        Question="What language did you first learn to speak?"
        self.MySurvey=AnonymousSurvey(Question)
        self.Responses=['English','Spanish','Mandarin']
    
    def testStoreSingleResponse(self):
        self.MySurvey.StoreResponse(self.Responses[0])
        self.assertIn(self.Responses[0],self.MySurvey.Responses)

    def testStoreThreeResponses(self):
        for Response in self.Responses:
            self.MySurvey.StoreResponse(Response)
        for Response in self.Responses:
            self.assertIn(Response,self.MySurvey.Responses)

unittest.main()
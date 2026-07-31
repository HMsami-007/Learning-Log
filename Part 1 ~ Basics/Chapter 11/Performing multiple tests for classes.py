import unittest
from DummyClass1 import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def testStoreSingleResponse(self):
        Question="What language did you first learn to speak?"
        MySurvey=AnonymousSurvey(Question)
        MySurvey.StoreResponse('English')
        self.assertIn('English',MySurvey.Responses)

    def testStoreThreeResponses(self):
        Question="What language did you first learn to speak?"
        MySurvey=AnonymousSurvey(Question)
        Responses=['English','Spanish','Mandarin']
        for Response in Responses:
            MySurvey.StoreResponse(Response)

        for Response in Responses:
            self.assertIn(Response,MySurvey.Responses)

unittest.main()
import unittest
from DummyClass1 import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def testStoreSingleResponse(self):
        Question="What language did you first learn to speak?"
        MySurvey=AnonymousSurvey(Question)
        MySurvey.StoreResponse('English')
        self.assertIn('English',MySurvey.Responses)

unittest.main()
import unittest
from DummyFunction2 import GetFormattedName
class NameTestCase(unittest.TestCase):
    def test_FirstLastName(self):       ##The unittest framework automatically scans your test classes for any functions starting with the exact prefix test. Because it saw a capital T on TestFirstLastName, it ignored the function entirely, resulting in Ran 0 tests.
        FormattedName=GetFormattedName("janis","joplin")
        self.assertEqual(FormattedName,"Janis Joplin")

unittest.main()
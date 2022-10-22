import unittest
from tanslator import english_to_french,french_to_english

class TestTranslatorModule(unittest.TestCase):
    """
    Class to the test the translator Module Created
    """
    def test_english_to_french(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Hello"),"Hello")

    def test_french_to_english(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Bonjour"),"Bonjour")

if __name__ == "__main__":
    unittest.main()
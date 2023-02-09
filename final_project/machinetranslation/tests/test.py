import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        """This test translator to translate from English to French"""
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('Goodbye'),'Au revoir')
    
    def test_frenchToEnglish(self):
        """This test translator to translate from French to English"""
        self.assertEqual(frenchToEnglish('Au revoir'),'Goodbye')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

if __name__=='__main__':
    unittest.main()

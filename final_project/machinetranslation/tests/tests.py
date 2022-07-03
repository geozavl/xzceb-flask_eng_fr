import unittest
import translator
from translator import english_to_french, french_to_english

class TestEmptyTranslationEF(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), 400)

class TestHelloTranslation(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), 'Bonjour')

class TestEmptyTranslationFE(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), 400)

class TestBonjourTranslation(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), 'Hello')

unittest.main()

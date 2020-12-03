from imdbURL import giveURL
import json
import unittest

class MyTest(unittest.TestCase):

    def test_giveURL(self):
        x = giveURL("300")
        y = giveURL("Scooby Doo")
        z = giveURL("titanic")
        a = giveURL("Before Night Falls")
        
        
        self.assertEqual(x, "https://www.imdb.com/title/tt0416449")
        self.assertEqual(y, "https://www.imdb.com/title/tt0267913")
        self.assertEqual(z, "https://www.imdb.com/title/tt0120338")
        self.assertEqual(a, "https://www.imdb.com/title/tt0247196")
        
unittest.main() 
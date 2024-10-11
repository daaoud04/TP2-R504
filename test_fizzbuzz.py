import unittest
from io import StringIO
import sys
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Rediriger la sortie vers un StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche()  # Appel de la fonction
        
        # Récupérer la sortie
        sys.stdout = sys.__stdout__  # Rétablir la sortie standard
        output = captured_output.getvalue().strip()
        
        # Vérifier que le début de la sortie est correct
        self.assertTrue(output.startswith("12"))
        self.assertTrue("Fizz" in output)
        self.assertTrue("Buzz" in output)
        self.assertTrue("FrisBee" in output)

if __name__ == "__main__":
    unittest.main()

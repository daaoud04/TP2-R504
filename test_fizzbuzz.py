import unittest
from io import StringIO
import sys
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_10_16(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche(10, 16)  # Appel de la fonction avec 10 et 16
        
        sys.stdout = sys.__stdout__  # Rétablir la sortie standard
        self.assertEqual(captured_output.getvalue().strip(), "Buzz11Fizz1314FrisBee")  # Vérifiez que cela correspond

    def test_fizzbuzz_5_10(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche(5, 10)  # Appel de la fonction avec 5 et 10
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "BuzzFizz78FizzBuzz")

if __name__ == "__main__":
    unittest.main()

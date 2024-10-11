import unittest
from io import StringIO
import sys
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_15(self):
        # Rediriger la sortie vers un StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche(15)  # Appel de la fonction avec 15
        
        # Récupérer la sortie
        sys.stdout = sys.__stdout__  # Rétablir la sortie standard
        self.assertEqual(captured_output.getvalue().strip(), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")

    def test_fizzbuzz_5(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche(5)  # Appel de la fonction avec 5
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "12Fizz4Buzz")

    def test_fizzbuzz_1(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche(1)  # Appel de la fonction avec 1
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1")

    def test_fizzbuzz_3(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche(3)  # Appel de la fonction avec 3
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "12Fizz")

if __name__ == "__main__":
    unittest.main()

import unittest
from io import StringIO
import sys
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Rediriger la sortie vers un StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        affiche()  # Appel de la fonction sans paramètres
        
        # Récupérer la sortie
        sys.stdout = sys.__stdout__  # Rétablir la sortie standard
        expected_output = (
            "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee1617Fizz"
            "19FizzBuzz22Fizz24FrisBee26Fizz28FizzBuzz31Fizz33"
            "FrisBee36Fizz38FizzBuzz41Fizz43FrisBee46Fizz48"
            "FizzBuzz51Fizz53FrisBee56Fizz58FizzBuzz61Fizz63"
            "FrisBee66Fizz68FizzBuzz71Fizz73FrisBee76Fizz78"
            "FizzBuzz81Fizz83FrisBee86Fizz88FizzBuzz91Fizz93"
            "FrisBee96Fizz98FizzBuzz"
        )
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()

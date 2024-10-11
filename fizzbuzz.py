def affiche(n1, n2):
    result = ""
    for i in range(n1, n2 + 1):
        if i % 15 == 0:
            result += "FrisBee"
        elif i % 3 == 0:
            result += "Fizz"
        elif i % 5 == 0:
            result += "Buzz"
        else:
            result += str(i)
    print(result)

# Exemples d'exécution
affiche(5, 10)  # Affiche : BuzzFizz78FizzBuzz
affiche(10, 16)  # Affiche : Buzz11Fizz1314FrisBee16

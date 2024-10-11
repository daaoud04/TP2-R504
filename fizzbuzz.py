def affiche(n1, n2):
    output = ""
    for i in range(n1, n2 + 1):
        if i % 15 == 0:
            output += "FrisBee"
        elif i % 3 == 0:
            output += "Fizz"
        elif i % 5 == 0:
            output += "Buzz"
        else:
            output += str(i)
    print(output)

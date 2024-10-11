def affiche(n):
    output = ""
    for i in range(1, n + 1):
        if i % 15 == 0:
            output += "FrisBee"
        elif i % 3 == 0:
            output += "Fizz"
        elif i % 5 == 0:
            output += "Buzz"
        else:
            output += str(i)
    print(output)

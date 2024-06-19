def factorialStack(number):
    if number == 1:
        return 1
    else:
        return number * factorialStack(number - 1)

print(factorialStack(7))
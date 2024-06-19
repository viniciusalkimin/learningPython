def factorialStack(number):
    if number == 1:
        return 1
    else:
        return number * factorialStack(number - 1)
def otherFactorial(num):
    total = num
    while num > 1:
        total = total*(num-1)
        num = num-1
    return total

print(otherFactorial(7))
print(factorialStack(7))
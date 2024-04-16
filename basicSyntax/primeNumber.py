def isPrimo(num: int):
    if num <=1:
        return False
    count: int = 0
    for n in range(1,num+1):
        if num%n==0:
            count+=1
    if count > 2:
        return False
    else:
        return True
    
def isPrimo1(num: int):
    if num <=1:
        return False
    for n in range(2, num):
        if(num%n==0):
            return False
    return True

number = 3
print(isPrimo(number))
print(isPrimo1(number))

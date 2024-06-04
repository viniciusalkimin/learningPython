def regressive(num):
    print(num)
    if num <= 0:
        return
    else:
        regressive(num - 1)

regressive(5)
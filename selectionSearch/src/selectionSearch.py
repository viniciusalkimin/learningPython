arr = [4,5,8,2,9,1]

def lowerNumber(arr):
    for a in range(len(arr)):
        lower = arr[a]
        indice = a
        for i in range(a + 1, len(arr)):
            if arr[i] < lower:
                lower = arr[i]
                indice = i

        other = arr[a]
        arr[a] = lower
        arr[indice] = other

lowerNumber(arr)

print(arr)
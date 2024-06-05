arr = [4,5,8,2,9,1]

def lowerNumber(arr):
    for a in range(len(arr)):
        lower = a
       # indice = a
        for i in range(a + 1, len(arr)):
            if arr[i] < arr[lower]:
                lower = i
                #indice = i

        other = arr[a]
        arr[a] = arr[lower]
        arr[lower] = other

lowerNumber(arr)

print(arr)
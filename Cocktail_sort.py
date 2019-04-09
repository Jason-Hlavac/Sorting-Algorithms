import random
numbers=[]
for i in range(random.randint(75,150)):
    numbers.append(random.randint(-10000,10000))
    
def cocktail(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if(arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
        for k in range(n):
            if(arr[i]> arr[k]):
                arr[i], arr[k] + arr[k], arr[i]
    print(arr)
    
cocktail(numbers)

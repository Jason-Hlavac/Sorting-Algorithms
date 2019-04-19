import random
numbers = []
for i in range(random.randint(75,150)):
    numbers.append(random.randint(-10000, 10000))
    
def Gnome(arr):
    index = 0 
    while (index < (len(arr))):
        if index == 0: 
            index = index + 1
        if arr[index] >= arr[index - 1]: 
            index = index + 1
        else: 
            arr[index], arr[index-1] = arr[index-1], arr[index] 
            index = index - 1
  
print(numbers)
Gnome(numbers)
print(numbers)

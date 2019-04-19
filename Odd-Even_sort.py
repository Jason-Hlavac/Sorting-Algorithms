import random
numbers = []
for i in range(random.randint(75,150)):
    numbers.append(random.randint(-10000, 10000))
def odd_even(arr):
    done = 0
    while(done == 0):
        done = 1
        for i in range(0, len(arr)-1, 2):
            if (arr[i] > arr[i+1]):
                arr[i],arr[i+1] = arr[i+1], arr[i]
                done = 0
        for i in range(1, len(arr)-1, 2):
            if (arr[i] > arr[i+1]):
                arr[i],arr[i+1] = arr[i+1], arr[i]
                done = 0
print(numbers)
odd_even(numbers)
print(numbers)

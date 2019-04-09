import random
numbers = []
array_a= 0
compares = 0
for i in range (random.randint(75,150)):
  numbers.append(random.randint(-10000,10000))
  
 for i in range (len(numbers)):
  for j in range (len(numbers)):
  
    if (numbers[i] < numbers[j]):
      numbers[i], numbers[j] = numbers[j], numbers[i]
     

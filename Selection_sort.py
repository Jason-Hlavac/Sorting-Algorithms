import random

numbers = []

for i in range (random.randint(75,150)):
	numbers.append(random.randint(-10000,10000))

def find_min(index,cindex, count):
	cindex = cindex + 1
	while (cindex < len(numbers)):
		if (numbers[index] > numbers[cindex]):
			index = cindex
		
		cindex = cindex + 1

	numbers[int(count)], numbers[index]=numbers[index], numbers[int(count)]
for i in range (len(numbers)):
	find_min(i,i,i)
	
print(numbers)

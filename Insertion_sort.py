import random

numbers = []

for i in range(random.randint(75,150)):
	numbers.append(random.randint(-10000,10000))

def insert(list):
	for i in range(len(list)):
		currentvalue = list[i]
		position = i
		while(position>0 and currentvalue<list[position-1]):
			list[position], list[position-1]=list[position-1],list[position]
			position -= 1
	
insert(numbers)
print (numbers)

import random

numbers = []

for i in range(random.randint(75,150)):
    numbers.append(random.randint(-10000, 10000))
print (numbers)    
def merge_sort(list):
    if len(list) > 1:
        mid = round(len(list)//2)
        l = list[mid:]
        r = list[:mid]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while (i < len(l)-1 and j < len(r)-1):
            if (l[i] < r[j]):
                list[k] = l[j]
                i+=1
            else:
                list[k] = r[j]
                j+=1
            k+=1
            
        while i < len(l)-1: 
            list[k] = l[i] 
            i+=1
            k+=1
          
        while j < len(r)-1: 
            list[k] = r[j] 
            j+=1
            k+=1
merge_sort(numbers)
print(numbers)

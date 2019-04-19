import random
numbers = []
for i in range(random.randint(75, 100)):
    numbers.append(random.randint(-10000, 10000))
    
def quick_sort(arr, low, high):
    if (low < high):
        pi = pivot(arr, low, high)
        quick_sort(arr, low, pi-1)
        pivot(arr, pi+1, high)
        
def pivot(arr, low, high):
    i = ( low-1 )         
    pivot = arr[high]      
  
    for j in range(low , high): 
  
        if   arr[j] <= pivot: 
          
            i += 1
            arr[i],arr[j] = arr[j],arr[i] 
            
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return ( i + 1 ) 
print (numbers)
quick_sort(numbers, 0, len(numbers)-1)
print (numbers)

""" Program 4  Write a program that does the bubble sort. Demonstrate its complexity 
by empirically calculating  the time to execute for arrays of size 1000 and 2000 
and show the difference.  Some useful commands:


import time
start_time = time.time()
import random
list4=[random.randint(0,10) for i in range(100)]
# The line above creates a random list of size 100 with values 0-10 inclusive """

import time
start_time = time.time()
import random

def bubble_sort(arr):
    if (len(arr) == 1):
        return arr
    
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]


    return arr

arr = [5,4,3,2,1]
list4=[random.randint(0,10) for i in range(100)]
print(arr)
print(bubble_sort(arr))


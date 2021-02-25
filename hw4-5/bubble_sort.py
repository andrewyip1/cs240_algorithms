import time
start_time = time.time()
import random

def bubble_sort(arr):
    if (len(arr) == 1):
        return arr
    
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]


    return arr

list1=[random.randint(0,10) for i in range(100)]
print(list1)
st1 = time.time()
print(bubble_sort(list1))
arr1time = time.time()-st1
print(arr1time)
print("\n")

list2=[random.randint(0,10) for i in range(100)]
print(list2)
st2 = time.time()
print(bubble_sort(list2))
arr2time = time.time()-st2
print(arr2time)
print("\n")

list3=[random.randint(0,10) for i in range(100)]
print(list3)
st3 = time.time()
print(bubble_sort(list3))
arr3time = time.time()-st3
print(arr3time)
print("\n")

list4=[random.randint(0,10) for i in range(100)]
print(list4)
st4 = time.time()
print(bubble_sort(list4))
arr4time = time.time()-st4
print(arr4time)
print("\n")

list4=[random.randint(0,10) for i in range(100)]
print(list4)
st4 = time.time()
print(bubble_sort(list4))
arr4time = time.time()-st4
print(arr4time)
print("\n")

print("This algorithm is O(n^2)")



import time
import random

#both of these algorithms return the index target is found at and -1 if not found

def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    
    while (left <= right):
        mid = (left+right)/2
        if (arr[mid] == target):
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

#list1 = [1,3,6,7,11,12,18,21]
#list2 = [2,5,3,7,1]
#list3 = sorted(list2)

#linear search for a big list
big_list = []
top = 2**21
for i in range(top):
    big_list.append(i)
linear_start = time.time()
print ('linear search of big list @ (index): ', linear_search(big_list, top-1))
print('time for linear search: ', time.time()-linear_start)

 #binary search for a big list
big_list2 = []
top2 = 2**21
for i in range (top2):
    big_list2.append(i)
binary_start = time.time()
print('binary search of a big list @ (index): ', binary_search(big_list2, top2-1))
print('time for binary search: ', time.time()-binary_start)




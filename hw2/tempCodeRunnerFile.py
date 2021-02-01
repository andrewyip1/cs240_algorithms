#Programming problem 1- (Compare Linear and Binary search )
#(Use Python's time method and try various sizes of lists. We will compare worst case cases 
#in both cases-(Am I repeating myself?) Lists will just consist of 1..n where n is a power of 2 - 
#(To make life easy-but I think the binary search method actually works for any n)
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
#big_list = []
#top = 2**25
#for i in range(top):
    #big_list.append(i)
#linear_start = time.time()
#print ('linear search of big list @ (index): ', linear_search(big_list, top-1))
#print('time for linear search: ', time.time()-linear_start)
""" temp = [1,2,3,4,5]
print(binary_search(temp, 3)) """

#binary search for a big list
#big_list2 = []
#top2 = 2**25
#for i in range (top2):
    #big_list2.append(i)
#binary_start = time.time()
#print('binary search of a big list @ (index): ', binary_search(big_list2, top2-1))
#print('time for binary search: ', time.time()-binary_start)

abc = [1,2,3,4,5,6,7,8,9,10]
print('start time here: ')
start_temp = time.time()
print('practice binary search', binary_search(abc, 10))
print(time.time() - start_temp)



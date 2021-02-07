""" Program 2  Write a function wrap_by_k ( lst, k) that wraps an array lst around by k values. 
so if lst = [1, 2, 3, 4, 5, 6, 7, 8] wrap_by_k(lst, 3)  returns [6, 7, 8, 1, 2, 3, 4, 5]
Qualification: You do not have the memory to create a new array-the wrapping must be done in the original array. 

Try this the straight forward way before you use the non-obvious hint below. Can you do it? 
(Note: you cannot use lst[ : k] or lst[k : ] since these require the implicit creation of subarrays.

How many swaps are required for an array of size n with  a wrap of k places? 
This method is O(?)


Non-obvious hint:  you can do this by using your reverse method. 
Useful Python features:

You can slice arrays as follows:

a) lst[ : 5] consists of the first 5 elements of lst
b) lst[5 : ] consists  of lst[5], lst[6], lst[7] ... etc
 """

def wrap_by_k(arr, num):
    temp = arr[len(arr)-num:] #storing the wrapped items
    original_front = arr[0: len(arr)-len(temp)]
    arr[0:len(temp)] = temp
    arr[len(temp):] = original_front
    return arr

def wrap_by_k_pt2 (arr, num):
    index = len(arr) - num
    return arr[index: ] + arr[: index]

def wrap_by_k_pt3(arr,num):
    for i in range (len(arr)-1, -1, -1):
        if (num > 0):
            arr.remove(arr[i])
            arr.insert(0, arr[i])
            num = num - 1
    return arr


arr = [1,2,3,4,5,6,7,8]
print(arr)
print(wrap_by_k(arr,3))



arr2 = [1,2,3,4,5,6,7,8]
print(arr2)
print(wrap_by_k(arr2,3))

arr3 = [1,2,3,4,5,6,7,8]
print(arr3)
print(wrap_by_k(arr3,3))


print("This method of O(n) and only takes one swap. ")

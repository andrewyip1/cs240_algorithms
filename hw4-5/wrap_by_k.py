"""Write a function wrap_by_k ( lst, k) that wraps an array lst around by k values. 
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

def wrap_by_k_pt4(arr, num=0):
    a = num%len(arr)
    return arr[-a:] + arr[:-a]


#MOST EFFICIENT WAY
def wrap_by_k_pt5(arr, num): #go up to k and rotate it by 1 to wrap around
    for i in range (num):
        rightRotateByOne(arr)
    return arr

def rightRotateByOne(arr):
    last = arr[len(arr)-1] #gets the last one that we're moving to the front
    for i in range (len(arr)-2, -1, -1): 
        arr[i+1] = arr[i] #moving each element up one index
    arr[0] = last #after the loop is done we move the last one to the front

arr = [1,2,3,4,5,6,7,8]
print(arr)
print(wrap_by_k(arr,3))
print("\n")

arr2 = [1,2,3,4,5,6,7,8]
print(arr2)
print(wrap_by_k(arr2,3))
print("\n")

arr3 = [1,2,3,4,5,6,7,8]
print(arr3)
print(wrap_by_k(arr3,3))
print("\n")

arr4 = [1,2,3,4,5,6,7,8]
print(arr4)
print(wrap_by_k(arr4,3))
print("\n")

arr5 = [1,2,3,4,5,6,7,8]
print(arr5)
print(wrap_by_k(arr5,3))
print("\n")

print("The time complexity is O(n)")

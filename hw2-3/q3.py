#recursive algorithms in class examples

#a - factorial
def factorial (num):
    if (num == 1):
        return 1
    return num*factorial(num-1)

#b - nth fibonacci sequence
def fibonacci (n):
    if (n <= 1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

#c - find the max or an array
def findMax(A):
    if len(A)==1:
        return A[0]
    else:
        if A[0] <= A[-1]: #if the last one is greater than the first element
            A = A[1:] #make the array smaller each time
            #print(A)
            return findMax(A)
        elif A[0] > A[-1]: #else if the first 1 is greater than the last one
            A = A[:-1] #go from the beginning to the last - 1 element
            #print(A)
            return findMax(A)

#d - find the max of an array
def max_recursive (A):
    n = len(A)
    if n <= 1:
        m = A[0] 
    else:
        #left side and right side
        m = max(max_recursive(A[:n//2]), max_recursive(A[n//2:]))
    return m

#e - search using binary search recursively
def binary_search_recursive (start, end, A, target):
    if (start >= end):
        return -1
    mid = (start+end)/2
    if (A[mid] == target):
        return mid
    elif (A[mid] > target):
        return binary_search_recursive(start, mid - 1, A, target)
    else:
        return binary_search_recursive(mid + 1, end, A, target)

#a - factorial
print('factorial recursively: ' , factorial(5))
#b - fibonacci sequence
print('fibonacci sequence of the nth value: ' , fibonacci(6))
#c - find max recursively
c = [4,6,18,12,5,7,8]
print('finding the max recursively (noah): ' , findMax(c))
#d - find max recursively
d = [4,6,18,12,5,7,8]
print('finding the max recursively (rick example): ' , max_recursive (d))
#e - binary search recursively
e = [1,3,5,7,9,10, 11, 15, 20,50, 54]
print('binary search recursively @ index : ' , binary_search_recursive(0, len(e)-1, e, 20))


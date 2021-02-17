""" Program 1 write a program that returns a reversed array. 
Qualification: Your chip has very limited memory so you do not have the memory to create a new array 
to store the reversed values. You must overwrite the original array.

Hopefully the following hint gives away how to do this:
hint and very useful feature of Python:
If you want to swap two values say x=2 and y=3 there is a really nice way to do this:
x, y = y, x

there is no need to use a temp variable!!  I like Python!
 """

def reverse_array(arr):
    if (len(arr) == 1):
        return arr

    back = len(arr)-1
    
    for i in range (len(arr)/2):
        arr[i], arr[back] = arr[back], arr[i]
        back = back - 1
    
    return arr

arr = [1,2,3,4,5]
print(arr)
print(reverse_array(arr))

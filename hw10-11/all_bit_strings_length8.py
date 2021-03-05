""" (Write a program that generates all bit strings of length 8 
with 3 1's and 5 0's. ie 00101100, 00010101 etc. 
Hint: use prob 4-How? Think about it then ask) """

# Function to print the output  
def printTheArray(arr, n):  

    zero_count = 0
    one_count = 0
    
    #to find the count of values
    for i in range(0, n):  
        if arr[i] == 0:
            zero_count = zero_count + 1
        else:
            one_count = one_count + 1
    
    if zero_count == 5 and one_count == 3:
        for i in range (n):  
            print(arr[i], end = " ")  
        print() 
  
# Function to generate all binary strings  
def generateAllBinaryStrings(n, arr, i):  
  
    if i == n: 
        printTheArray(arr, n)  
        return
      
    # First assign "0" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)  
  
    # And then assign "1" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)  
  

#Main 
n = 8
arr = [None] * n  
  
# Print all binary strings  
generateAllBinaryStrings(n, arr, 0)  
  
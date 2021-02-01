#Programming problem 2- (largest_subarray_sum)
#Write the program that finds the largest sum of a contiguous subarray of integers. ie (See directions following 
#examples a and b)

#a) [34, -50, 42, 14, -5, 86] should return 137 since [42, 14, -5, 86] is the largest sum for consecutive elements.

#b) [10, -12, 4, 8, 6, -20, 2, 4] should return 18 since [4, 8, 6] is the largest sum for consecutive elements.

#Note: if all the elements are positive it would be the sum of the entire array

#2a) Do this the straight forward way by considering all possible contiguous subset sums. What will the order of 
# this method be? (explain why) Note -you need to vary the start index, the end index, and then compare the 
# sums of each of these for the maximum sum.

#2b) Use a strategy suggested by product_without and smallest_window 
# to come up with a method that is O(n). In other words you should be able to solve this by using no nested loops. 
# (Hint: you need to keep track of running values of something like in programs 1 and 2.

# 2A o(n^3)
def largest_subarray_2a (arr):
    sum = 0
    left = 0
    right = 0
    for i in range(len(arr)): #start point
        for j in range(len(arr)-1,-1,-1): #end point
            tempSum = 0
            for x in range(i,j+1):
                tempSum += arr[x]
            if (tempSum > sum):
                sum = tempSum
                left = i
                right = j
    return sum

#2B o(n)
def largest_subarray_sum(arr):
    curr = 0
    max_sum = arr[0]

    for i in range (len(arr)):
        curr = max(arr[i], arr[i]+curr)
        max_sum = max(max_sum, curr)
    return max_sum

a = [34,-50,42,14,-5,86]
b = [10, -12, 4, 8, 6, -20, 2, 4] 

print('sum of largest sub-array o(n) - arrA' , largest_subarray_sum(a))
print('sum of largest sub-array o(n) - arrB' , largest_subarray_sum(b))

print('sum of largest sub-array o(n^3) - arrA' , largest_subarray_2a(a))
print('sum of largest sub-array o(n^3) - arrB' , largest_subarray_2a(b))
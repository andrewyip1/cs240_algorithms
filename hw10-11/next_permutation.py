""" Write the program that generates the next permutation of (1,2,3...,n) in lexicographic order.  """
def next_permutation (arr):
    
    i = len(arr)-1
    first_decrease = -1
    temp = [] #to store all values until you see a decrease (going from right to left)
    start_change_index = -1

    #we go from right to left to find the first value at which there is a decrease
    while i >= 0:
        if arr[i-1] < arr[i]:
            temp.append(arr[i])
            first_decrease = arr[i-1]
            start_change_index = i-1
            break #stop as soon as we see a decrease
        else:
            temp.append(arr[i])
        i = i - 1
    
    temp.append(first_decrease)
    temp.sort()

    #for loop that finds next value after first decrease
    for i in range (len(temp)):
        if temp[i] > first_decrease: #finding the value that is greater than the first decrease on the right side
            arr[start_change_index] = temp[i] #change the value to the next greatest vlaue
            temp.remove(arr[start_change_index]) #remove that value from the temporary array so we don't have repeats
            break
            
    res = arr[0:start_change_index+1] + temp
    return res


a = [4,6,2,5,3,1]
b = [8,7,9,3,6,5,4,3,2,1]

print(a)
print(next_permutation(a))

print(b)
print(next_permutation(b))

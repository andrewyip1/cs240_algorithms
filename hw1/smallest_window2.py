def smallest_window(arr):

    #set min/max at an infinite number to start out (have to do this because its not sorted)
    min = float('inf')
    max = float('-inf') #same thing as max_so_far

    #set left and right index to a number that is not a possible index
    left = -1
    right = -1

    #to find the right most spot 
    for i in range(len(arr)):
        if arr[i] > max: #increasing as you go along the array
            max = arr[i]
        else: #the last spot at which arr[i] < max (last spot)
            right = i #the very last 'yes' that occurs in the diagram/table
    
    #instead of thinking as left to right, think of as right to left
    #going to find min
    for i in range (len(arr)-1, -1, -1):
        if arr[i] < min:
            min = arr[i]
        else:
            left = i
    #for i in reversed(range(len(arr))):
        #if min > arr[i]:
         #   min = arr[i]
       # else:
         #   left = i
    
    print('left: '), left
    print('right: '), right

arr = [3,7,5,6,9]
smallest_window(arr) 
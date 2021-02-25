def longest_increasing_decreasing (arr):
    longest_increase = 1
    curr_increase = 1
    longest_decrease = 1
    curr_decrease = 1

    for i in range (0, len(arr)-1, 1):
        if arr[i+1] > arr[i]:
            curr_decrease = 1
            curr_increase = curr_increase + 1
            longest_increase = max(longest_increase, curr_increase)
        else: 
            curr_increase = 1
            curr_decrease = curr_decrease + 1
            longest_decrease = max(longest_decrease, curr_decrease)
    
    print("longest increase: " , longest_increase)
    print("longest decrease: ", longest_decrease)  

arr = [1,2,4,3,2,5,7,8,12,8,13,14,12,8,6,4,2,3,4] 
longest_increasing_decreasing(arr)

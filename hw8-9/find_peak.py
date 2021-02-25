def find_peak (arr):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return arr[0]
    
    curr_peak = arr[0] 
    for i in range (1, len(arr)-1):
        if arr[i] > curr_peak: 
            curr_peak = arr[i] #updates curr_peak every time the if statement is satisfied
        else:
            return curr_peak #if the if statement is not satisfied it returns curr_peak
    return curr_peak

def find_peak_pt2(arr):
    curr_index = 0
    while arr[curr_index+1] < arr[curr_index]: #checks the next one to see that it is greater than the current
        curr_index = curr_index + 1
    return arr[curr_index] 

arr=[2,3,4,6,7,8,3,2]
print(find_peak(arr))

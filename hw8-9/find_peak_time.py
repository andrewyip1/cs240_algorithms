import time

def find_peak (arr):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return arr[0]
    
    curr_peak = arr[0] 
    for i in range (1, len(arr)-1):
        if arr[i] > curr_peak:
            curr_peak = arr[i]
        else:
            return curr_peak
    return curr_peak

arr = []
for i in range (2**24):
    arr.append(i)
arr.append(0)
start_time = time.time()
print(find_peak(arr))
print("Time: " , time.time() - start_time)

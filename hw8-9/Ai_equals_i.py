
def Ai_equals_i (arr):

    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

def Ai_equals_i_pt2(arr):
    mid_index = len(arr)//2
    if (mid_index == arr[mid_index]):
        return mid_index
    elif mid_index > arr[mid_index]: #IF INDEX GREATER THAN VALUE, SEARCH RIGHT
        return Ai_equals_i_pt2(arr[mid_index:])
    elif mid_index < arr[mid_index]: #IF VALUE GREATER THAN INDEX, SEARCH LEFT, since the index increases by 1, and the array is sorted, the value will always be greater than the index so we search the left side
        return Ai_equals_i_pt2(arr[: mid_index])
    else:
        return -1

arr = [-4,-3,1,2,4,8,9,10,11,12,14,18,19,22,50,51]
print(Ai_equals_i(arr))
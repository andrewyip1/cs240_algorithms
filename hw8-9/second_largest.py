def second_largest (arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr[len(arr)-2]

def second_largest_pt2 (arr):
    max_so_far = arr[0]
    second_largest = arr[0]

    for i in range (1,len(arr)):
        if arr[i] > max_so_far:
            second_largest = max_so_far
            max_so_far = arr[i]
        elif arr[i] > second_largest and arr[i] < max_so_far:
            second_largest = arr[i]
            
    return second_largest

def second_largest_pt3 (arr):
    arr.sort()
    return arr[-2]

arr=[1,2,4,3,2,5,7,8,12,8,13,14,12,8,6,4,2,3,4]
arr2 = [4,7,2,3,9,1,6,0]
print(second_largest(arr2))
print(second_largest_pt2(arr))
print(second_largest_pt3(arr))
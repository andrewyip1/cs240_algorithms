# What is an inversion?
# An inversion is when a[i] > a[j] and i < j
# Time complexity: O(nlogn)

def merge_sort(A, temp, left, right):
    inversion_count = 0
    if left < right:
        mid = (left+right)//2  # calculating mid point
        merge_sort(A, temp, left, mid)  # sorts left subarray
        merge_sort(A, temp, mid + 1, right)  # sorts right subarray
        inversion_count += merge(A, temp, left, mid, right)
    return inversion_count


def merge(A, temp, left, mid, right):
    inversion_count = 0  # what we return
    i = left  # left half of array
    j = mid + 1  # right half of array
    index = left  # iterating through array

    # merging two arrays
    while i <= mid and j <= right:
        if A[i] <= A[j]:  # smaller value is on the left side
            temp[index] = A[i]
            i += 1
            index += 1
        else:  # smaller value is on right side
            temp[index] = A[j]
            inversion_count += (mid-i+1)
            j += 1
            index += 1

    # remaining left elements
    while i <= mid:
        temp[index] = A[i]
        i += 1
        index += 1

    # remaining right elements
    while j <= right:
        temp[index] = A[j]
        j += 1
        index += 1

    # replacing elements in temp back to original array
    for i in range(left, right+1):
        A[i] = temp[i]

    # print(A)
    print("# of inversions: ", inversion_count)
    return inversion_count


A = [4, 2, 1, 7, 6, 5, 3, 0]
temp = [0]*len(A)
print("Total # of inversion: ", merge_sort(A, temp, 0, len(A)-1))

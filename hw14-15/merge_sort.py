def merge_sort(A, temp, left, right):
    if right > left:
        mid = (left+right)//2
        merge_sort(A, temp, left, mid)  # sorts the left subarray
        merge_sort(A, temp, mid + 1, right)  # sorts the right subarray
        merge(A, temp, left, mid, right)  # returns merged sorted array
    return A


def merge(A, temp, left, mid, right):
    i = left
    j = mid + 1
    index = left

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp[index] = A[i]
            i += 1
        else:
            temp[index] = A[j]
            j += 1
        index += 1

    # remaining elements
    while i <= mid:
        temp[index] = A[i]
        i += 1
        index += 1

    while j <= right:
        temp[index] = A[j]
        j += 1
        index += 1

    # transfer temp back to original
    for i in range(left, right + 1):
        A[i] = temp[i]

    return A


A = [1, 2, 4, 7, 0, 3, 5, 6]
temp = [0]*len(A)
print(merge_sort(A, temp, 0, len(A)-1))

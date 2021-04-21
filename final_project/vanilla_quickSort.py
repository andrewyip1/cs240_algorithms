# Vanilla QuickSort-pivot is always first element

# partition
import random
import time


def partition(A, left, r):
    pivot = A[left]  # the pivot value is always the first value
    i = left+1
    for j in range(left+1, r):  # going from left to right
        if A[j] < pivot:
            #print("j:", j)
            # print(A)
            A[j], A[i] = A[i], A[j]
            # print(A)
            # print()
            i = i+1
    A[left], A[i-1] = A[i-1], A[left]
    #print("done partition function")
    return i-1


def quicksort(A, left, r):
    if left >= r:  # when lower and upper indexes meet
        return

    i = left
    j = partition(A, left, r)   # Then do the partitioning

    # left partition
    quicksort(A, left, j)      # 2 recursive calls- this one from left to j-1

    # right partition
    quicksort(A, j+1, r)    # This one from j+1 to the end of the array


# Driver Code
#A = [3, 8, 2, 5, 1, 4, 7, 6]

#A = []


# appending to list
# for i in range(20000):
#A.append(random.randint(1, 1000))

# 5 times running
for i in range(5):
    # creating list
    A = []
    # for i in range(800, 0, -1):
    # A.append(i)

    for i in range(20000):
        A.append(random.randint(1, 1000))

    # print(A)

    # shuffling 5 times
    # for i in range(len(A)):
    #   firstIndex = random.randint(0, len(A)-1)
    #  secondIndex = random.randint(0, len(A)-1)
    # A[firstIndex], A[secondIndex] = A[secondIndex], A[firstIndex]

    # for i in range(0, len(A), len(A)//10):
    # for j in range(i, i+len(A)//10, 1):
    #firstIndex = random.randint(i, i+len(A)//10-1)
    #secondIndex = random.randint(i, i+len(A)//10-1)
    #A[firstIndex], A[secondIndex] = A[secondIndex], A[firstIndex]

    st = time.time()
    quicksort(A, 0, len(A))
    print(time.time()-st)


#st = time.time()
#quicksort(A, 0, len(A))
# print(A)
#print("time it took:", time.time()-st)

#quicksort(A, 0, len(A))
# print(A)

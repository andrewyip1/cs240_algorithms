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
    A[left], A[i-1] = A[i-1], A[left]  # swap lower index with pivot value
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


list2 = [random.randint(0, 1000) for i in range(80000)]
# Part 1
""" list1=[]
for i in range(320000):
    list1.append(i) """
# Part 2 and 3
""" for i in range(len(list2)):
    firstNum = random.randint(0,len(list2)-1)
    secondNum = random.randint(0,len(list2)-1)
    list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum] """
# Part 4
""" for i in range(0, len(list2), len(list2)//10):
    for j in range(i, i+len(list2)//10, 1):
        firstNum = random.randint(i, i+len(list2)//10-1)
        secondNum = random.randint(i, i+len(list2)//10-1)
        list2[firstNum],list2[secondNum] = list2[secondNum], list2[firstNum] """
# Part 6
""" list1 = []
for i in range(800,0,-1):
    list1.append(i) """
# Part 5
""" list2 = [random.randint(0, 1000) for i in range(320000)]
for i in range(160):
    list2.append(random.randint(0, len(list2)-1))
start_time = time.time()
quicksort(list2, 0, len(list2))
print("Time taken: ", time.time()-start_time) """

import random
import time

# ANALYZING QUICK SORT'S TIME COMPLEXITY


def quicksort(A, left, right):
    if left >= right:
        return

    # pivot = A[random.randint(left, right)]  # random pivot point
    pivot = A[left]  # left pivot point
    # pivot = A[(left+right)//2] # middle pivot point
    index = partition(A, left, right, pivot)

    # recursively call on left and right
    quicksort(A, left, index-1)
    quicksort(A, index, right)
    return A


def partition(A, left, right, pivot):
    while left <= right:

        while A[left] < pivot:
            left = left + 1

        while A[right] > pivot:
            right = right - 1

        if left <= right:
            A[left], A[right] = A[right], A[left]
            left = left + 1
            right = right - 1

    return left


# PART 1
""" 1) arrays of various sizes that are completely sorted to begin with.  Notice you will need to use 
different n values to illustrate this. What about O(n) or O(n*log(n)) behavior? Will some arrays 
exhibit O(n^2) behavior? """

""" for i in range(5):

    # creating the list
    A = []
    for i in range(20000):
        A.append(random.randint(1, 1000))

    A.sort()

    st = time.time()
    quicksort(A, 0, len(A)-1)
    print(time.time()-st) """


# PART 2
""" 2. arrays of various sizes that are almost sorted. Maybe 5% or 10% of the array 
elements are out of order. Define what it means for 5% to be out of order """

""" for i in range(5):

    n = 40000

    # fill array with values from 1-1000
    A = []
    for i in range(n):
        A.append(i)

    # arrays is already sorted

    # shuffling the first (5% of the length)
    for i in range(int(len(A)*.05)):
        firstNum = random.randint(0, len(A)-1)
        secondNum = random.randint(0, len(A)-1)
        A[firstNum], A[secondNum] = A[secondNum], A[firstNum]

    st = time.time()
    quicksort(A, 0, len(A)-1)
    print(time.time()-st) """


# PART 3
""" 3. arrays of various sizes that are well shuffled. Use a shuffle routine 
that does n shuffles on an array of size n. YOU MUST WRITE YOUR OWN SHUFFLE ROUTINE. """

""" for i in range(5):

    n = 20000

    # fill array with values from 1-1000
    A = []
    for i in range(n):
        A.append(random.randint(1, 1000))

    # shuffling (100% of the length)
    for i in range(len(A)):
        firstNum = random.randint(0, len(A)-1)
        secondNum = random.randint(0, len(A)-1)
        A[firstNum], A[secondNum] = A[secondNum], A[firstNum]

    st = time.time()
    quicksort(A, 0, len(A)-1)
    print(time.time()-st) """


# PART 4
""" 4. What about the array being shuffled in sections? 
ie the 1st 10 % is shuffled amongst its values, and the second 10% is likewise shuffled etc """


""" for i in range(5):

    list2 = []
    n = 20000
    for i in range(n):
        list2.append(i)  # list is already sorted

    for i in range(0, len(list2), len(list2)//10):
        for j in range(i, i+len(list2)//10, 1):
            firstNum = random.randint(i, i+len(list2)//10-1)
            secondNum = random.randint(i, i+len(list2)//10-1)
            list2[firstNum], list2[secondNum] = list2[secondNum], list2[firstNum]

    st = time.time()
    quicksort(list2, 0, len(list2)-1)
    print(time.time()-st) """

# PART 5
""" 5. What about an array that has new values added to the end -or front of an array """

""" for i in range(5):

    list2 = []
    n = 20000
    for i in range(n):
        list2.append(i)  # sorted list

    # looking at last 10% (add to front and end)
    print(len(list2)-len(list2)*.1)
    for i in range(int(len(list2)-len(list2)*.1), int(len(list2))):
        temp = list2[int(len(list2)-len(list2)*.1): int(len(list2))]  # last 10%
        temp.sort()
        list2.insert(0, random.randint(temp[0], temp[len(temp)-1])) """

#st = time.time()
#quicksort(list2, 0, len(list2)-1)
# print(time.time()-st)

# PART 6
""" 6. What about an array sorted backwards? """

""" for i in range(5):

    list2 = []
    n = 20000
    for i in range(n, 0, -1):
        list2.append(i)  # backwards

    st = time.time()
    quicksort(list2, 0, len(list2)-1)
    print(time.time()-st) """

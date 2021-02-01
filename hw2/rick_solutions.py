import time
import random
# Some recursive programs
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1)*n


#print(fact(5))


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


# for i in range(1, 8):
#     print(fibo(i))


def findMax(A):
    print(A[0]," ",A[1:],"\n")
    n = len(A)
    if n <= 1:
        return A[0]
    else:
        return max(findMax(A[1:]), A[0])


A = [5, 12, 7, 18, 7, 6, 4, 1]
#print(findMax(A))


def findMaxBin(A):
    n = len(A)
    print(A[0:n//2]," ",A[n//2:],"\n")
    if n <= 1:
        return A[0]
    else:
        return max(findMaxBin(A[:n//2]), findMaxBin(A[n//2:]))


print(findMaxBin(A))
#test for how bad 

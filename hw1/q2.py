#Write the program that finds the smallest "window" that needs to be sorted in an 
#array in order for the entire array to be sorted. So given the array 
#A = [3,7,5,6,9] you should return left = 1 and right = 3 since the 
#elements A[1], A[2], and A[3] are out of order. Use the algorithm 
#discussed in class which requires 2 passes through the array.

a = [3,7,5,6,9]
b = []
b.extend(a)
b.sort()
left = -1
right = -1

#finding the first out of place spot
for i in range(len(a)):
    if (a[i] != b[i]):
        left = i
        break

#finding the spot from the back that is out of place
for i in range (len(a)-1, -1, -1):
    if (a[i] != b[i]):
        right = i
        break

print('left: '), left
print('right: '), right

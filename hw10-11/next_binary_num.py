""" Write the program that generates the next binary number for a bit string of length n. """
import random

def next_binary_num (num1):

    a = num1
    b = "1"

    b = b.zfill(len(num1))

    #initialize the result
    result = ""

    #initialize the carry
    carry = 0

    print('a ' , a)
    print('b ' , b)
    print("\n")

    #traverse backwards
    for i in range (len(a)-1, -1, -1):
        
        if int(a[i])+int(b[i])+carry == 0:
            result += "0"
            carry = 0
        elif int(a[i])+int(b[i])+carry == 1:
            result += "1"
            carry = 0
        elif int(a[i])+int(b[i])+carry == 2:
            result += "0"
            carry = 1
        elif int(a[i])+int(b[i])+carry == 3:
            result += "1"
            carry = 1

    if carry != 0:
        result += str(carry)
    
    return result[::-1] 

def next_binary_num_pt2 (num1):
    length = len(num1)
    num = list(num1)

    #going from right to left
    index = length-1
    while index >= 0:
        if num[index] == '0': #changing the 0's to a 1's
            num[index] = '1'
            break
        else: #changing 1's to 0's
            num[index] = '0' 
        index = index - 1
    
    num1 = ''.join(num) #converting list back into string

    #IF STRING IS ALL 1'S
    if index < 0: #if index is -1 
        num1 = '1' + num1
    return num1


A = [0,1] #array of 0 and 1
n = 3 #length of binary string
num = ""
for i in range (n):
    num += str(A[random.randint(0,1)])

print(num)
print(next_binary_num(num))
print("\n")

num2 = ""
for i in range (n):
    num2+= str(A[random.randint(0,1)])
print(num2)
print(next_binary_num_pt2(num2))


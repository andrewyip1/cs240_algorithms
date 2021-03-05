#determine the probability of two numbers (x,y) being relatively prime
import random

def euclidean_alg (x, y):
    if x == 0:
        return y
    
    res = y % x
    y = x
    x = res
    return euclidean_alg(x, y)

count = 0

for i in range (100):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print("1st Number: " , num1)
    print("2nd Number: ", num2)
    val = euclidean_alg(num1, num2)
    print(val)
    if val == 1:
        count = count + 1

print("# of times GCD is equal to 1: " , count)
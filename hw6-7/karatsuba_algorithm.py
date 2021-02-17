
#multiply two long numbers together
#divide and conquer 
import math

def karatsuba(x,y):

    # Base Case:
    if x < 10 and y < 10:
        return x*y

    n = max(int(math.log10(x)+1),int(math.log10(y+0.001)+1))
    half_n = int(n//2) #how we split up in half

    #Defining xA, xB, yC, yD
    xA = int(x // 10**half_n) #Dividing 'x' into first half
    xB = int(x % 10**half_n) #Dividing 'x' into second half
    yC = int(y // 10**half_n) #Dividng 'y' into first half
    yD = int(y % 10**half_n) #Dividing 'y' into second half

    #Defining ac, bd, abcd, and the difference
    ac = karatsuba(xA,yC) #AC: Step 1: First recursive call
    bd = karatsuba(xB,yD) #BD: Step 2: Second recursive call
    ab_cd = karatsuba(xA + xB, yC + yD) #Step 3: Third recursive call (a+b) (c+d)
    S4 = ab_cd-bd-ac #Gauss's Trick - calculating the difference

    #Main Equation - x*y = ((10^n) * ac) + ((10^n/2) * (ad + bd)) + bd
    return int((10**(half_n*2)*ac) + (10**half_n)*S4 + bd)

print(karatsuba(1234567891011121314151617181920212223242526272829303132333435363,1357911131517192123252729313335373941434547495153555759616365676))



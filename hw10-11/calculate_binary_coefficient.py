""" Is there a relationship between n and k that will indicate for what values of n and k C(n,k) 
will be odd? Write a program to compute the binomial coefficients efficiently(ie at no place 
in your code should k! be used)  for various values of n and k and propose a hypothesis  """

def nCr (n, k):

    if (k > n):
        return -1
    
    numerator = 1
    denominator = 1
    for i in range (k):
        numerator *= (n-i)
        denominator *= (k-i)
    
    return numerator//denominator

n = 10
k = 5
print(nCr(n,k))

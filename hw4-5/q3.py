""" Program 3 How many 0's are at the end of 100! That's 100 factorial not 100 with an exclamation! Do this 
without calculating 100! Write an efficient  
general method that determines the number of 0's at the end of n!. For instance 10! = 3,628,800 has 2. 
Your method is what order?  """

#CALCULATE HOW MANY 0's AT THE END OF n!

def count_trailingZeros(n):

    #initialize count
    count = 0

    #keep dividing n by powers of 5 and update count
    i = 5
    while(n/i >=1):
        count += int(n/i)
        i*=5 #powers of 5 each time
    
    return int(count)

n = 25
print('how many zeros at the end of ' , n , '!')
print(count_trailingZeros(n))
print("The time complexity is O(log(n))")

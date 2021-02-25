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

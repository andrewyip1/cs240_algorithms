""" Write a program that generates all bit strings of length 8 with 3 1's 
and 5 0's. ie 00101100, 00010101  """

#C(8,3) = 56
#n = 8
#r = 3 (we are choosing 3 1's)

#Finds the first index at which you add to from the right
def find_index(next_r_combinations,n):
    r = len(next_r_combinations)
    index = r #start from the back

    #checks the current last element in the next_r_combinations
    # if that value is less than the last value in the larger list, 
    # n, we return that index that needs to be changed
    while(next_r_combinations[index-1] == n-r+index): #find the closest value on the right that is not equal to n
        index += -1

    return index-1

#Increase the value of next_r_combination[find_index] by 1
# and each value after that by 1
def next_combo(next_r_combinations,n):
    r = len(next_r_combinations)
    j = find_index(next_r_combinations,n) #index at which we start to change values from right on

    #Retrieves the left most position at which we increment by 1 that we need to change
    next_r_combinations[j] += 1 #increment that index by 1

    #increments the next element in array by the current value + 1
    for k in range(j,r-1): # going from the index we need to change to the length -1 
        next_r_combinations[k+1] = next_r_combinations[k]+1 #increments the next element in array by the current value + 1
    #Returns sample array with new combination
    return next_r_combinations

def construct_bit_strings (next_r_combinations, n):
    bit_strings = [] #the list of bit strings length 8
    for i in range(n+1):
        bit_strings.append(0) #adding 

    #going through the list of indexes to place 1 at
    for i in range (len(next_r_combinations)):
        bit_strings[next_r_combinations[i]] = 1
    return bit_strings
    
#Find the next r combinations of 1,2,...n
next_r_combinations = [0,1,2] # 0 - (r-1) value
n = 7

print(next_r_combinations)
print(construct_bit_strings(next_r_combinations, n))
print("\n")

for i in range(55):
    next_r_combinations = next_combo(next_r_combinations,n) #list of indexes
    print(next_r_combinations)
    print(construct_bit_strings(next_r_combinations, n))
    print("\n")
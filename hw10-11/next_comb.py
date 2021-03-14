""" Write the program that generates the next r combination  of (1,2,3...,n) in 
lexicographic order- ie if n =6 and r=4 next_comb([1,2,3,6]) should return [1,2,4,5]. 
Use your program to generate all 15 4-combinations of [1,2,3,4,5,6]  """

#C(6,4) = 15

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

#Find the next resulting r combinations from 1 to n
next_r_combinations = [1,2,3,4] #values from 1 to r
n = 6
print("combination #" , 1)
print(next_r_combinations)
print("\n")

for i in range(14):
    next_r_combinations = next_combo(next_r_combinations,n) #reassigning next_r_combinations each iteration
    print("combination #" , i+2)
    print(next_r_combinations)
    print("\n")

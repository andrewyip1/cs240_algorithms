#Multiply the following binary numbers 
#10010011 * 01100110
def add_binary(a,b):

    #add zeros to the shorter one up to the length of the longer binary number
    longer_len = max(len(a), len(b))
    a = a.zfill(longer_len)
    b = b.zfill(longer_len)

    #initialize the result
    result = ""

    #initialize the carry
    carry = 0

    #traverse backwards
    for i in range (longer_len-1, -1, -1):
        
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
        result += carry
    
    return result[::-1]

def multiply_binary_num (a, b):

    # since both are the same length, we just need to find the length of one
    res = ""
    place_binary = ""

    #find product of two binary numbers
    # traversing the bottom multiplier
    for i in range (len(b)-1, -1 , -1): 
        place_binary = ""
        #add appropriate zeros depending on what place you're at (10's, 100's, etc...)
        for x in range (len(b)-1 - i):
            place_binary += "0"

        #traversing the top multiplier
        for j in range (len(a)-1, -1, -1): # going through top multiplier
            if int(b[i])*int(a[j]) == 1:
                place_binary += "1"
            else:
                place_binary += "0"
        res += place_binary[::-1] + "\n" # adds the backwards string and adds it to a new line

    #somehow split into array using split by "\n"
    all_nums = res.split("\n")
    all_nums.pop() #removes the last one
    for i in range (len(all_nums)-1):
        all_nums[i+1] = add_binary(all_nums[i], all_nums[i+1])
    
    return all_nums[len(all_nums)-1]

print ("PRODUCT: " , multiply_binary_num("1001", "101"))

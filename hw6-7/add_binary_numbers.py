def add_binary(a,b):

    #add zeros to the front of the shorter binary input up to the length of the longer binary number
    longer_len = max(len(a), len(b))
    a = a.zfill(longer_len)
    b = b.zfill(longer_len)

    #initialize the result
    result = ""

    #initialize the carry
    carry = 0

    print(a)
    print(b)
    print("\n")

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
        result += str(carry)
    
    return result[::-1]

print(add_binary("1110", "1011"))
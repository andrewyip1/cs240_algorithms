#Write the program that converts any decimal integer to it's base b expansion. b<10

def convert_decimal_base_b (num, base):
    
    if base > 10:
        return -1
    
    base_num = ""
    while (num > 0):

        dig = int(num%base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters

        #changing the quotient each time
        num = num // base
        
    return base_num[::-1]

print(convert_decimal_base_b(22, 2))

    
#using string input
def binary_to_decimal (n):
    exponent = 0
    decimalVal = 0
    for i in range (len(n)-1, -1, -1):
        if n[i] == "0":
            decimalVal += 0
            exponent += 1
        else:
            decimalVal += 2**exponent
            exponent += 1
    return decimalVal

#using integer input
def binary_to_decimal_pt2 (n):
    decimal = 0
    exponent = 0
    while (n > 0):
        decimal += ((2**exponent) * (n%10))
        n //= 10
        exponent = exponent + 1
    return decimal

print(binary_to_decimal("1110100"))
print(binary_to_decimal_pt2(1110100))
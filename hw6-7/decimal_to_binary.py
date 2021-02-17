def decimal_to_binary (n):
    highest_exponent = 0
    iteration = 0

    while True:
        if n >= 2**iteration:
            highest_exponent = iteration
            iteration = iteration + 1
        else:
            highest_exponent = iteration - 1
            break

    res = ""
    while n >= 0 and highest_exponent >= 0:
        if n >= 2**highest_exponent:
            res += "1"
            n = n-2**highest_exponent
            highest_exponent = highest_exponent - 1
        else:
            res += "0"
            highest_exponent = highest_exponent - 1
    return res

#shorter way (better way)
def decimal_to_binary_pt2(n):
    base_num = ""
    while n > 0:
        digit = str(n%2)
        base_num += digit
    return base_num[::-1]

print(decimal_to_binary(231))
print(decimal_to_binary(100))



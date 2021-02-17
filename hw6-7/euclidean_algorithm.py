def euclidean_algorithm (x, y):

    if x == 0:
        return y
    
    res = y % x
    y = x
    x = res
    return euclidean_algorithm(x, y)

print(euclidean_algorithm(1, 5))
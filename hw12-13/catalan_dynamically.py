# Find a recurrence relation for Cn, the number of ways to parenthesize the product of n + 1 numbers, x0 · x1 · x2 · ··· · xn,
# to specify the order of multiplication. For example, C3 = 5 because
# there are five ways to parenthesize x0 · x1 · x2 · x3 to determine the order of multiplication:
#
# ((x0 · x1) · x2) · x3
# (x0 · (x1 · x2)) · x3
# (x0 · x1) · (x2 · x3)
# x0 · ((x1 · x2) · x3)
# x0 · (x1 · (x2 · x3))

def catalan_dynamically(n):

    if n <= 1:
        return 1

    # initializing array
    catalan_vals = [0]*(n+1)

    # initialize first two values
    catalan_vals[0] = 1
    catalan_vals[1] = 1

    # filling in the values up to n
    # finding sum for each n value from 2 to n
    for current_n_value in range(2, n + 1):
        # inner loop doing calculation from 0 to current n - 1 (according to formula)
        for k in range(current_n_value):
            catalan_vals[current_n_value] += catalan_vals[k] * \
                catalan_vals[current_n_value-k-1]

    return catalan_vals[n]


n = 3
print(catalan_dynamically(n))

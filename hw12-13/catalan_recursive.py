# Find a recurrence relation for Cn, the number of ways to parenthesize the product of n + 1 numbers, x0 · x1 · x2 · ··· · xn,
# to specify the order of multiplication. For example, C3 = 5 because
# there are five ways to parenthesize x0 · x1 · x2 · x3 to determine the order of multiplication:
#
# ((x0 · x1) · x2) · x3
# (x0 · (x1 · x2)) · x3
# (x0 · x1) · (x2 · x3)
# x0 · ((x1 · x2) · x3)
# x0 · (x1 · (x2 · x3))


def catlan_recursive(n):

    global count
    count += 1

    if n <= 1:  # when n = 0, 1
        return 1

    val = 0
    for k in range(n):  # sum from k to n
        val += catlan_recursive(k)*catlan_recursive(n-k-1)

    return val


n = 10
count = 0  # to count how many times recursive call happens
for i in range(n+1):
    print(catlan_recursive(i))

print("# times recursively called: ", count)

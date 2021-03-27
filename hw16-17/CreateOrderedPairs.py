import decimal
import operator
import matplotlib.pyplot as plt
#import pandas.plotting._matplotlib as plt


a = (6, 2, 4, 3, 7, 5)
b = (13, 25, 47, 11, 92, 68)

# Create a list of ordered pairs-ie tuples
c = list(zip(b, a))
print(c)

print(c[2])  # Print the 3rd ordered pair
print(c[2][0])  # Print the 1st element in the 3rd ordered pair


# The following are 2 diff ways to sort based on which
# value you are sorting on.
Px = sorted(c, key=operator.itemgetter(0))  # -(c is a list of tuples)
print(Px)

Py = sorted(c, key=lambda x: x[1])
print(Py)

plt.scatter(b, a)
plt.show()

# Might be useful to unzip a list of ordered tuples-
# so you could scatterplot the ordered tuples - Let us know
# if you are able to discover a way to do this

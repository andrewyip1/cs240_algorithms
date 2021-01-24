#Write the program discussed in class that is O(n) ie it only requires 
#single loops rather than nested loops to find an array of products of an array, 
#save for the ith element. So [1,2,3,4,5] returns [120, 60, 40, 30,24]. 
#Your computer lacks a division routine.

#initial array
a = [1,2,3,4,5]
print ('initial array: ') , a

#creating a left_products and right_products product array
left_products = [None] * len(a)
right_products = [None] * len(a)
res = [None] * len(a) #resulting array

#to the left_products and right_products_products we set it to 1
left_products[0] = 1 #starting at the left_products
right_products[len(right_products) -1] = 1 #starting at the right_products

#filling the left_products array
for i in range (1, len(left_products)):
    left_products[i] = a[i-1]*left_products[i-1]
print ('left_products: '), left_products

#filling the right_products array
for i in range (len(right_products)-2, -1, -1):
    right_products[i] = a[i+1]*right_products[i+1]
print('right_products: '), right_products

#resultant array
for i in range (len(a)):
    res[i] = left_products[i]*right_products[i]
print('product array: '), res



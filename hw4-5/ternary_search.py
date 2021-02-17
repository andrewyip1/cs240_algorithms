# Function to perform Ternary Search
def ternary_search(left, right, target, arr):
	if (right >= left):
		# Find the mid1 and mid2
		mid1 = left + (right - left) //3
		mid2 = right - (right - left) //3
		# Check if target is present at any mid
		if (arr[mid1] == target): 
			return mid1
		if (arr[mid2] == target): 
			return mid2
		
		# Since targetis not present at mid,
		# check in which region it is present
		# then repeat the Search operation
		# in that region
		if (target < arr[mid1]): 
			# The targetlies in between l and mid1
			return ternary_search(left, mid1 - 1, target, arr)
		
		elif (target > arr[mid2]): 
			# The target lies in between mid2 and r
			return ternary_search(mid2 + 1, right, target, arr)
		
		else: 
			# The target lies in between mid1 and mid2
			return ternary_search(mid1 + 1, 
								mid2 - 1, target, arr)
	# target not found
	return -1

# array has to be sorted
arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Search the array using ternary_search
p = ternary_search(0, len(arr)-1, 10, arr)

# Print the result
print("Index of", 10, "is", p)


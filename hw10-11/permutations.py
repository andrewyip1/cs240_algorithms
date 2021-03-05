# print all permutations recursively
def permutations(lst):
    if len(lst) == 1:
        return lst
    
    list1 = []

    for i in range(len(lst)):
        m = lst[i]
        small_lst = lst[:i] + lst[i+1:] #left over list

        #recursively call for leftover elements to find all permutations
        for p in permutations(small_lst):
            list1.append([m] + [p])
    return list1

# calling permutations
a = [1, 2, 3]
print(a)
for i in range(6):
    print("index: ", i)
    print(permutations(a)[i])
    print("\n")
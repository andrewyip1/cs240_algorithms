def smallest_window(nums):

    nums2 = []
    nums2.extend(nums)
    nums2.sort()
    start = len(nums)-1
    end = 0
    for i in range (len(nums)):
        if (nums[i] != nums2[i]):
            start = min(i, start)
            end = max(i, end)
    
    print('start: '), start
    print('end: '), end


arr = [3,7,5,6,9]
smallest_window(arr)

# [3,7,5,6,9]
# [3,5,6,7,9]
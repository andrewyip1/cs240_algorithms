def merge_sort (arr):
    
    if len(arr) > 1: 

        #midpoint
        mid = len(arr)//2

        #splitting arrays in half each time
        left_half = arr[:mid]
        right_half = arr[mid:]

        #recursive calls
        merge_sort(left_half)
        merge_sort(right_half)

        #values to traverse the left and right arrays
        left = 0
        right = 0
        index = 0

        #going through both arrays. exits once one reaches the end
        while left < len(left_half) and right < len(right_half):
            if left_half[left] < right_half[right]:
                arr[index] = left_half[left]
                left = left + 1
            else:
                arr[index] = right_half[right]
                right = right + 1
            index = index + 1
        
        #remaining elements IF there is any on the left side
        while left < len(left_half):
            arr[index] = left_half[left]
            left = left + 1
            index = index + 1
        
        #remaining elements IF there is any on the right side
        while right < len(right_half):
            arr[index] = right_half[right]
            right = right + 1
            index = index + 1

        return arr

A =[64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,33,32,31,30,29,28,27,26,25,24,23,22,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
B =[32,31,30,29,28,27,26,25,24,23,22,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
C = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
print(merge_sort(A))
print(merge_sort(B))
print(merge_sort(C))



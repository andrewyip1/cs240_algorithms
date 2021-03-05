""" How many bit strings? Find a recursive formula for the the number of bit 
strings of length n that contain 2 consecutive 0's: Hint: there are 3 different 
ways this sequence can start:
with a 1, or with a 01, or a 00.  """

def how_many_pairs_zeros (num):

    print(num)

    if len(num) < 2:
        return 0
    else:
        if num[0] == "0" and num[1] == "0":
            return 1 + how_many_pairs_zeros(num[1:])
        else:
            return 0 + how_many_pairs_zeros(num[1:])


print("count of how many pairs of 0's: " , how_many_pairs_zeros("1100010"))

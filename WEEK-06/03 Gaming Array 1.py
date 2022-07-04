#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def helper(array):
    maximum = float('-inf')
    result  = 0
    for ele in array:
        if ele > maximum:
             maximum = ele
             result += 1
             
    return result

def gamingArray(arr):
    return 'ANDY' if helper(arr) % 2 == 0 else 'BOB'

# Kunal Wadhwa

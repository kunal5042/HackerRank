#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    left = [None for x in arr]
    right = [None for x in arr]
    
    left[0] = arr[0]
    for idx in range(1, len(arr)):
        left[idx] = left[idx-1] + arr[idx]

    right[len(right)-1] = arr[len(arr)-1]
    for idx in reversed(range(len(arr)-1)):
        right[idx] = right[idx+1] + arr[idx]

    for idx in range(len(arr)):
        if left[idx] == right[idx]:
            return 'YES'

    return 'NO'

# Kunal Wadhwa

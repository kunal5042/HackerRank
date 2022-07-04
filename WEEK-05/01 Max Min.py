#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    result = float('inf')
    
    # -k because, otherwise we will get index out of bound
    # +1 because zero indexed array
    for idx in range(len(arr) -k + 1):
        
        # idx +k because we want the max element of that subarray
        # idx +k and -1 because zero indexed arary
        result = min(result, arr[idx +k -1] - arr[idx])
        
    return result
   
# Kunal Wadhwa
# 6621 1445 5286


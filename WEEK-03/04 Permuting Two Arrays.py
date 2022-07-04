#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    for idx in range(len(A)):
        if A[idx] + B[idx] < k:
            return 'NO'
    return 'YES'

# Kunal Wadhwa

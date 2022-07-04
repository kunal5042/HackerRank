#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    result = float('inf')
    arr.sort()

    for idx in range(1, len(arr)):
        diff = abs(arr[idx]-arr[idx-1])
        if diff < result:
            result = diff

    return result

# Kunal Wadhwa

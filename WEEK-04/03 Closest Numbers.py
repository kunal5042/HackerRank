#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
#
def closestNumbers(arr):
    arr.sort()
    minimum = float('inf')
    result = []

    for idx in range(1, len(arr)):
        closest = abs(arr[idx] - arr[idx-1])

        if closest == minimum:
            result.append(arr[idx-1])
            result.append(arr[idx])
            continue

        if closest < minimum:
            result.clear()
            minimum = closest
            result.append(arr[idx-1])
            result.append(arr[idx])

    return result

# Kunal Wadhwa
# 6621 1445 5286

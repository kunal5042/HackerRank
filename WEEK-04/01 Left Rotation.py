#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # what I'm basically doing is removing the element from the start
    # and pushing it back to the end
    
    for _ in range(d):
        arr.append(arr.pop(0))
    
    return arr

# Kunal Wadhwa

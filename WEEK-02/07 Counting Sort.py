#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    frequency = [0 for x in range(100)]
    
    for ele in arr:
        frequency[ele] += 1
        
    return frequency

# Kunal Wadhwa
# 6621 1445 5286
#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#



def sansaXor(arr):
    # if the nubmer is even XOR = 0
    if len(arr)%2==0:
        return 0

    # if it's an odd length array, answer = XOR of every alternate number
    result = arr[0]
    for idx in range(2,len(arr),2):
        result = result ^ arr[idx]
        
    return result

# Kunal Wadhwa
# 6621 1445 5286

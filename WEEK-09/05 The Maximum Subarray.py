
#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    def kadane(arr):
        dynamic_sum = arr[0]
        max_sum     = arr[0]
        
        for ele in arr[1:]:
            dynamic_sum = max(ele, dynamic_sum + ele)
            max_sum     = max(dynamic_sum, max_sum)
            
        return max_sum
    
    def subseq(arr):
        result = 0
        
        for ele in arr:
            if ele > 0: result += ele
            
        if result == 0: result = max(arr)
        
        return result
    
    return [kadane(arr), subseq(arr)]

# Kunal Wadhwa

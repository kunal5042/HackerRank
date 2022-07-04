#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = {}
    result = 0
    for ele in ar:
        pairs[ele] = pairs.get(ele, 0) + 1
        
    for key, value in pairs.items():
        result += value // 2
    
    return result

# Kunal Wadhwa
# 6621 1445 5286
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    counts = {'positive':0, 'negative':0, 'zeroes': 0}
    for ele in arr:
        if ele >  0: counts['positive'] += 1
        if ele <  0: counts['negative'] += 1
        if ele == 0: counts['zeroes'] += 1
    
    # positive ratio
    print(counts['positive']/len(arr))
    
    # negative ratio
    print(counts['negative']/len(arr))
    
    # zeroes
    print(counts['zeroes']/len(arr))
    
# Kunal Wadhwa
# 6621 1445 5286

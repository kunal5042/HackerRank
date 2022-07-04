#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    result = [0, 0]
    
    # first game
    min_max = [scores[0], scores[0]]
    
    for ele in scores[1:]:
        cur_min = min_max[0]
        cur_max = min_max[1]
        
        min_max[0] = min(cur_min, ele)
        min_max[1] = max(cur_max, ele)
        
        if min_max[0] != cur_min: result[0] += 1
        if min_max[1] != cur_max: result[1] += 1
    
    result.reverse()
    return result

# Kunal Wadhwa

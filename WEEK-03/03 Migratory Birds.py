#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    id_frequency_map = {}
    
    for idx, ele in enumerate(arr):
        id_frequency_map[ele] = id_frequency_map.get(ele, 0) + 1
    
    result = None
    max_sighted = float('-inf')
    
    for key, value in id_frequency_map.items():
        if value == max_sighted:
            result = min(result, key)
            
        if max_sighted < value:
            max_sighted = value
            result = key
            
    return result
        
# Kunal Wadhwa

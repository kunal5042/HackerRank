# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    (fre_map, fre_map2) = ({}, {})

    for char in s: fre_map[char] = fre_map.get(char, 0) + 1
    for value in fre_map.values(): fre_map2[value] = fre_map2.get(value, 0) + 1
        
    size = len(fre_map2.values())

    if size == 1: return 'YES'
    
    if size == 2:
        tuples = [(key, value) for (key, value) in fre_map2.items()]
        tuples.sort(reverse=True, key=lambda x: x[1])
        
        if tuples[1][1] == 1 and tuples[1][0] == 1: return 'YES'
        if tuples[1][1] == 1 and abs(tuples[1][0] - tuples[0][0]) == 1: return 'YES'
    
    return 'NO'
# Kunal Wadhwa

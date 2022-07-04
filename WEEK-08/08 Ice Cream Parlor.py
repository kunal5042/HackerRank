#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    map = {}
    for idx, price in enumerate(arr):
        if m - price in map:
            return [map[m-price], idx+1]
        map[price] = idx+1
        
# Kunal Wadhwa

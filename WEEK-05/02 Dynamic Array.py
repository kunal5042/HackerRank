#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # declare a 2D arrayay
    array = [[] for _ in range(n)] 
        
    # initialize lastAnswer to zero 
    lastAnswer = 0
    answers = []
    
    # given queries
    for query in queries:
        
        # format of the query
        (queryType, x, y) = (query[0], query[1], query[2])
        
        # idx format
        idx = ((x ^ lastAnswer) % n)
        
        # what we have been asked to do
        # simply put
        if queryType == 1:
            array[idx] += [y]
        else:
            lastAnswer = array[idx][y % len(array[idx])]
            answers.append(lastAnswer)
        
    return answers

# Kunal Wadhwa

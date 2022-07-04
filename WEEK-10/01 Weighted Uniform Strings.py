#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#
import string

def weightedUniformStrings(s, queries):
    weight = 1
    weights = {}    
    
    alphas = string.ascii_lowercase
    
    # fill in the hash_map of weights of all the ascii lowercase characters
    for alpha in alphas:
        weights[alpha] = weight
        weight += 1
        
        
    # calculate the weights of all the uniform substrings and store in hash map
    # initializing hash map for that
    uniform_weights = {}
    
    # starting with alpha at idx 0 in string s
    # current alpha's weight
    alpha_weight = weights[s[0]]

    # current uniform substring's weight
    uniform_weight = alpha_weight

    # storing the current uniform substring's character in a buffer var
    # current alpha
    buffer = s[0]
    
    # to store the result
    result = []
    
    for idx in range(1, len(s)):
        # if this conditions is true
        # the current substring is still uniform 
        if s[idx] == buffer:
            # update the map of uniform weights
            uniform_weights[uniform_weight] = buffer
            # update the current uniform string's weight
            uniform_weight += alpha_weight
            
        else:
            # insert the weight of last uniform substring
            uniform_weights[uniform_weight] = buffer
            
            # now change the buffer
            buffer = s[idx]
            alpha_weight = weights[s[idx]]
            # new uniform substring's weight is equal to current character's weight
            uniform_weight = alpha_weight
            
    # the last uniform weight would not have been added to the map
    # so, add it explicitly 
    uniform_weights[uniform_weight] = buffer
        
    # check if the query is present in uniform_weights hash map
    for query in queries:
        if query in uniform_weights:
            result.append('Yes')
        else:
            result.append('No')
        
    return result

# Kunal Wadhwa

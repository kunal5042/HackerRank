#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(height, width):
    mod = 10 ** 9 + 7
    
    valid_perms = [0] * (width + 1)
    valid_perms[0] = 1
    
    for w in range(1, width + 1):
        valid_perms[w] = sum(valid_perms[max(0, w - 4):w])
        valid_perms[w] %= mod
        
    for w in range(width + 1):
        valid_perms[w] = valid_perms[w] ** height
        valid_perms[w] %= mod
        
    valid = valid_perms[:]
    
    for w in range(len(valid)):
        for separator in range(1, w):
            valid[w] -= valid[separator] * valid_perms[w-separator]
            
        valid[w] %= mod
        
    return valid[width]

# Kunal Wadhwa

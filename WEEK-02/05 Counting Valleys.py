#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    tracker = 1 if path[0] == 'U' else -1
    for p in path[1:]:
        down = False
        
        if tracker < 0: down = True
        
        if p == 'D':
            tracker -= 1
        else:
            tracker += 1
        
        if tracker == 0 and down is True:
            valleys += 1
            
    return valleys

# Kunal Wadhwa
# 6621 1445 5286
#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    
    for idx in range(len(grid)):
        # convert the string into a list
        grid[idx] = list(grid[idx])
        # sort the list
        grid[idx].sort()
        
    # in every column, check if the characters are sorted
    for column in range(1, len(grid[0])):
        for row in range(1, len(grid)):
            # ord will return an integer value for the given character, so we will be able to compare it
            previous = ord(grid[row-1][column])
            current  = ord(grid[row][column])
            
            # if not sorted, return false
            if current < previous:
                return 'NO'
            
    # if we didn't return 'NO' yet, means it's sorted
    return 'YES'

# Kunal Wadhwa

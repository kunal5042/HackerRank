#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    (diagonal1, diagonal2) = (0, 0)
    (x_axis, y_axis) = (0, 0)
    
    while x_axis < len(arr):
        diagonal1 += arr[x_axis][x_axis]
        print(arr[x_axis][x_axis])
        x_axis += 1
        
    (x_axis, y_axis) = (0, len(arr)-1)
    
    while x_axis < len(arr) and y_axis >= 0:
        diagonal2 += arr[x_axis][y_axis]
        print(arr[x_axis][y_axis])
        x_axis += 1
        y_axis -= 1
            
    return abs(diagonal2 - diagonal1)

# Kunal Wadhwa

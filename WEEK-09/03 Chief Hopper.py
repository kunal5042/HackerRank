#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    # Write your code here
    BE=0
    for height in reversed(arr):
        BE = math.ceil((BE+height)/2)
        
    return BE
# Kunal Wadhwa

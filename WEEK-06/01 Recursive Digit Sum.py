#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    # Write your code here
    num_sum = 0
    for char in n:
        num_sum += int(char)
        
    # (n)k string 
    num_sum = num_sum * k
    
    return helper(str(num_sum))
    

def helper(num_string):
    if len(num_string) == 1:
        return int(num_string)
    
    num_sum = 0
    for char in num_string:
        num_sum += int(char)
        
    return helper(str(num_sum))

# Kunal Wadhwa
# 6621 1445 5286

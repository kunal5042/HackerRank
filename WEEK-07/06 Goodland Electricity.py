#
# Complete the 'pylons' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    greed = True          
    for a in range(k-1,-1,-1):
        if arr[a]==1:
            greed = False
            break
        
    if greed is True:
        return (-1)
               
    result = 1
    while a<len(arr)-k:
        a = a + 2*(k-1) + 1
        greed = True
        for i in range(2*(k-1)+1):
            if arr[min(a-i,len(arr)-1)]==1:
                result +=1
                a = a - i
                greed = False
                break
        if greed ==True:
            return (-1)
        
    return (result) 

# Kunal Wadhwa

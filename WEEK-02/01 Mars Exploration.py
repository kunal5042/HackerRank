#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # write your code here
    message = 'SOS'
    result = 0
    
    for idx in range(len(s)):
        if s[idx] != message[idx%3]:
            result += 1
            
    return result

# Kunal Wadhwa
# 6621 1445 5286
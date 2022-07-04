#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    # to note: in this question, subarray doesn't mean a solid subarray
    # the creater of this question should have mentioned that
    # I have written the solution that should work for a solid subarray, and that's why I'm sorting the array
    # This increases the time complexity from O(n) to O(nlog(n)) -.-
    a.sort()
    result = -1
    (cur_max, cur_min, cur_len) = (a[0], a[0], 1)
    
    for ele in a[1:]:
        if (abs(ele-cur_max)<=1) and (abs(ele-cur_min)<=1):
            cur_len += 1
            cur_max = max(cur_max, ele)
            cur_min = min(cur_min, ele)
            if cur_len >= 2:
                result = max(result, cur_len)

        else:
            cur_len = 1
            cur_max = ele
            cur_min = ele
    
    return result

# Kunal Wadhwa

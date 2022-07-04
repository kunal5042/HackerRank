#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    ways = 0
    for idx in range(len(s)):
        seg_sum = 0
        seg_cnt = 0
        for jdx in range(idx, idx+m):
            if jdx < len(s):
                seg_sum += s[jdx]
                seg_cnt += 1
                if seg_sum == d and seg_cnt == m:
                    ways += 1
    return ways

# Kunal Wadhwa

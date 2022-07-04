#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
# DP Solution
# Create a DP array of solutions of ways to change coins until n
# Refer back to the previous solutions when counting current coin
def getWays(n, coins):
    dp = [0] * (n + 1) 
    dp[0] = 1 # One way to return 0 coins
    
    for coin in sorted(coins):
        for idx in range(len(dp)):
            if coin <= idx: dp[idx] += dp[idx - coin]  
    
    return dp[-1]

# Kunal Wadhwa

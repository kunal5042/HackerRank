
#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    next_largest = [-1 for x in range(len(prices))]
    
    # next largest[idx] = prices[idx]'s next largest element in the array prices
    # fill the array
    # second last element's next largest will be
    # either the last element or the element itself
    # depending upon the condition 
    # if second_largest > or < than the last
    # to compare and store we use the largest variable
    largest = prices[len(prices)-1]
    for idx in reversed(range(len(prices)-1)):
        if prices[idx] > largest:
            largest = prices[idx]
        else:
            next_largest[idx] = largest
            
    # if next_largest[idx] for current price is -1
    # means we can't get profit if we buy today
    # else if, we have the price on the day we are gonna sell it
    # stored in next_largest[idx]; subtract the price today from it
    # and add it to the profit
    profit = 0
    for idx in range(len(next_largest)):
        if next_largest[idx] != -1:
            profit += (next_largest[idx] - prices[idx])
            
    return profit

# Kunal Wadhwa

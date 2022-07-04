#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # I came to this solution after working out multiple examples

    # so, basically, if both players are to pick the best move
    # player 2 can only win under two conditions

    # condition 1: Player 1 can't even make the first move, that is: towers length = 1 at the start
    if m == 1:
        return 2

    # condition 2: Player 2 can win if there are even number of towers
    if n % 2 == 0:
        return 2

    # in every other scenario, player 1 can win
    return 1

# Kunal Wadhwa
# 6621 1445 5286

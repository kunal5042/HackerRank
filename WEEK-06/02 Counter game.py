#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def smaller_power(number, result=1):
    while result < number:
        result *= 2
    
    result /= 2
    return result

def counterGame(n):
    turn = 0

    while n != 1:
        if n % 2 == 0:
            n /= 2
        
        else:
            n -= smaller_power(n)

        turn += 1

    
    return 'Louise' if turn % 2 != 0 else 'Richard'

# Kunal Wadhwa
# 6621 1445 5286

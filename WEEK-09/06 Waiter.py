#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def getQprimes(q):
    n = 2
    count = 0; out = []
    while(count < q):
        isPrime = True
        for i in range(2,n//2+1):
            if n%i == 0:
                isPrime = False
                break
        if isPrime:
            out.append(n)
            count += 1
        n += 1
    return out  


def waiter(number, q):
    primes = getQprimes(q); answer = []
    # Write your code here
    for i in primes:
        B = []; A = []
        for j in reversed(number):
            if j%i == 0:
                B.append(j)
            else: 
                A.append(j)
        number = A
        answer += reversed(B)
        
    answer += reversed(A)
    return answer

# Kunal Wadhwa

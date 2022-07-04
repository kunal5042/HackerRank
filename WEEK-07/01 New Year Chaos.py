# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # using bubble sort, get the array back to it's initial state
    # number of swaps will be = to number of bribes
    bribes = 0
    
    # keep track of individual element's number of swaps
    # if it exceeded 2, return 'Too chaotic'
    bribes_map = {}
    
    for i in range(len(q)):
        swaps = True
        for j in range(len(q)-1):
            if q[j] > q[j+1]:
                bribes_map[q[j]] = bribes_map.get(q[j],0)+1

                if bribes_map[q[j]] > 2:
                    print('Too chaotic')
                    return
                
                q[j], q[j+1] = q[j+1], q[j]
                bribes +=1
                
                swaps = False
        
        # optimization
        if swaps is True:
            print(bribes)
            return
    
    print(bribes)
    return

# Kunal Wadhwa

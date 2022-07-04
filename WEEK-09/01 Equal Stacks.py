def largest_common(a1, a2, a3):
    (hash2, hash3) = (set(a2), set(a3))
    common = []
    for ele in a1:
        if ele in hash2 and ele in hash3: common.append(ele)
    
    if len(common): return max(common)
    return 0
    
def equalStacks(h1, h2, h3):
    # Write your code here
    (len_h1, len_h2, len_h3) = (len(h1), len(h2), len(h3))
    
    sum1 = [0 for x in range(len_h1)]
    sum2 = [0 for x in range(len_h2)]
    sum3 = [0 for x in range(len_h3)]
    
    (sum1[len_h1-1], sum2[len_h2-1], sum3[len_h3-1]) =\
    (h1[len_h1-1], h2[len_h2-1], h3[len_h3-1])
    
    for idx in reversed(range(len_h1-1)):
        sum1[idx] = h1[idx] + sum1[idx+1]
        
    for idx in reversed(range(len_h2-1)):
        sum2[idx] = h2[idx] + sum2[idx+1]
        
    for idx in reversed(range(len_h3-1)):
        sum3[idx] = h3[idx] + sum3[idx+1]
        
    return largest_common(sum1, sum2, sum3)
    
# Kunal Wadhwa

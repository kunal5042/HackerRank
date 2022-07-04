def missingNumbers(arr, brr):
    # Write your code here
    result = []
    map_brr = {}
    
    # build a frequency map for all the numbers in the original array
    for number in brr:
        map_brr[number] = map_brr.get(number, 0) + 1
    
    # update the frequency map as follows
    # frequency(element x in brr) - frequency(element x in arr) NOTE: if element x in arr
    # else can't change, don't change
    for number in arr:
        map_brr[number] -= 1
        
    # if frequency of x in the map equals zero
    # that means frequency of x is same in both arrays
    # if not, means it's missing
    # add all the missing elements to the resultant array
    for key, value in map_brr.items():
        if value != 0:
            result.append(key)
    
    # sort the resultant array before returning
    result.sort()
    return result

# Kunal Wadhwa
# 6621 1445 5286

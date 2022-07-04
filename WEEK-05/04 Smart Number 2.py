import math

def is_smart_number(num):
    # Logic: 
    # if a number divided by it's square root equals the square root of that number
    # that number has odd number of factors
    val = int(math.sqrt(num))
    
    if num / val == val:
        return True
    
        return False

# getting the input and running the above function
for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



# Kunal Wadhwa
# 6621 1445 5286

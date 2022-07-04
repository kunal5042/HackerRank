#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# if an open bracket matches the respective close bracket: return True else: False
def match(open, close):
    if open == '{' and close == '}':
        return True
    
    if open == '(' and close == ')':
        return True
    
    if open == '[' and close == ']':
        return True
    
    return False

def isBalanced(s):
    stack = []
    open_brackets = '{ [ ('
    
    for bracket in s:
        # if a bracket is open type, append it to the stack
        if open_brackets.find(bracket) != -1:
            stack.append(bracket)
            
        else:
            # if there are no brackets to pop(): return False because unmatched brackets are there
            if len(stack) == 0:
                return 'NO'
            
            else:
                open = stack.pop()
                close = bracket
                # if a closing bracket doesn't match with most recent open bracket, return False:
                if match(open, close) is False:
                    return 'NO'
    
    # if there are no remaining unmatched brackets in the stack: return True
    if len(stack) == 0:
        return 'YES'
    
    return 'NO'

# Kunal Wadhwa

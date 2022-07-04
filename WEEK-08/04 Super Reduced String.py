#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    string = list(s)
    # to push all the distinct characters in the stack
    stack = [s[0]]
    
    # lambda expresison to compare stack top with current
    stack_top = lambda x: x[len(x)-1]
    
    for idx in range(1, len(string)):
        # if stack is empty, we can't pair the current character with any others
        if len(stack) != 0:
            # if current doesn't pair with stack top, push it
            if string[idx] != stack_top(stack):
                stack.append(string[idx])
                
            else:
                # if it does, pop it
                stack.pop()
        else:
            # if stack is empty, push the current
            stack.append(string[idx])
            
    if len(stack) == 0:
        # if all paired up, return empty string
        return 'Empty String'
    
    # else, return the string of remaining unpaired characters
    return ''.join(stack)

# Kunal Wadhwa

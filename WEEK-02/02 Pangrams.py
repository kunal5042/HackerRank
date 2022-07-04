#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabets = {}
    
    for character in s:
        if character != ' ':
            alphabets[character.lower()] = alphabets.get(character.lower(), True)
        
    print(alphabets)
    print(len(alphabets))
        
    if len(alphabets) == 26:
        return 'pangram'
    
    return 'not pangram'

# Kunal Wadhwa
# 6621 1445 5286
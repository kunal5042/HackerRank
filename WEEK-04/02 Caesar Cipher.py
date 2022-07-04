#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def caesarCipher(s, k):
    string = s
    key    = k
    # Write your code here
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    alpha_str = 'abcdefghijklmnopqrstuvwxyz'
    
    result = ''
    for char in string:
        # Algorithm
        # Find the index of the current character in the list of alphabets
        # Resultant element's index in the alphabets list will be the circular incrementaion of the current character's index
        # Append the new character to the result 
        if alpha_str.find(char) != -1:
                result += alphabets[ (alphabets.index(char) + key) % 26 ]
        else:
            # it could be an upper case character or a special character
            if alpha_str.find(char.lower()) != -1:
                # uppercase
                result += alphabets[ (alphabets.index(char.lower()) + key) % 26 ].upper()
            else:
                # special
                result += char
            
    return result

# Kunal Wadhwa

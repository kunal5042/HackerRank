# Returns 32-bit binary number for a given decimal number
# Accepts an integer value
# Returns a binary number representation in the form of a list
def decimal_to_binary(number):
    if number == 0:
        return [0 for x in range(32)]
    
    stack = []
    while number > 0:
        stack.append(number % 2)
        number = number // 2
    
    binary = []
    while len(stack) > 0:
        binary.append(stack.pop())
    
    # conver to 32-bit representation
    binary_32_bit = [0 for x in range(32)]
    idx = len(binary_32_bit) - 1
    
    for jdx in reversed(range(len(binary))):
        binary_32_bit[idx] = binary[jdx]
        idx -= 1
    
    return binary_32_bit 

# Accepts 32-bit binary number respresentation in the form of a list
# Returns the decimal number in the form of long integer
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for ele in reversed(binary):
        if ele == 1:
            decimal += 2**power
        power += 1
    return decimal

# Accepts 32-bit binary number respresentation in the form of a list
# Returns the binary number after flipping all ones with zeroes and vice versa
def flip_bits(binary):
    for idx, ele in enumerate(binary):
        if ele == 1: binary[idx] = 0
        if ele == 0: binary[idx] = 1
    return binary

# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
def flippingBits(n):
    # Write your code here
    return binary_to_decimal(flip_bits(decimal_to_binary(n)))

# Kunal Wadhwa
# 6621 1445 5286
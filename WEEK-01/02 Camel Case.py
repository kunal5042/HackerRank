inputs = []

while True:
    try:
        instruction = input()
        inputs.append(instruction)
    except:
        break
    
for idx, instruction in enumerate(inputs):
    # necessary step other-wise there are errors in parsing the input
    inputs[idx] = inputs[idx].strip('\n\r')
    
def split_function(string, operand_type='V'):
    capitals = [0]
    for idx in range(1, len(string)):
        if string[idx].isupper():
            capitals.append(idx)
    
    result = ''
    for parts_idx in range(1, len(capitals)):
        result += string[capitals[parts_idx-1]:capitals[parts_idx]] + ' '
    
    result += string[capitals.pop():]
    
    if operand_type == 'M':
        result = result[:-2]
        
    return result.lower()

def combine(string, taip='V'):
    result = ''
    words = string.split()
    for idx in range(len(words)):
        words[idx] = words[idx][0].upper() + words[idx][1:]
        result += words[idx]
    
    if taip == 'M':
        result = result[0].lower() + result[1:] + '()'
    elif taip == 'V':
        result = result[0].lower() + result[1:]
    else:
        pass

    return result

if __name__ == '__main__':
    for instruction in inputs:
        operation = instruction[0]
        operand_type = instruction[2]
        operand = instruction[4:]
        
        if operation == 'S':
            result = split_function(operand, operand_type)
        
        if operation == 'C':
            result = combine(operand, operand_type)
            
        print(result)

    
# Kunal Wadhwa
# 6621 1445 5286
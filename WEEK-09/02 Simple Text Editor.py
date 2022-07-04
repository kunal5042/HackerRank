# run the instruction
def run(ops, par):
    if ops == 1:
        append(par)
    elif ops == 2:
        delete(int(par))
    elif ops == 3:
        prnt(int(par))
    else:
        undo()

# empty string at the start
S = ''

# stack for undo
stack = [S]

# append function
def append(W):
    global S
    global stack
    S += W
    stack.append(S)
    #print(stack)
# delete
def delete(k):
    global S
    global stack
    S = S[:-k]
    stack.append(S)
    #print(stack)
    
# print
def prnt(k):
    global S
    if k-1 <= len(S):
        print(S[k-1])
    else:
        print("")
# undo
def undo():
    global S
    global stack
    S = stack.pop()
    S = stack[len(stack)-1]
    #print(stack)

# getting the input
no_of_operations =  input()
operations = []
for _ in range(int(no_of_operations)):
    operations.append(input())

# parsing the input
for instruction in operations:
    instruction = instruction.split()
    if len(instruction) < 2:
        ops = int(instruction[0])
        run(ops, None)
    else:
        ops = int(instruction[0])
        par = instruction[1]
        run(ops, par)

# Kunal Wadhwa

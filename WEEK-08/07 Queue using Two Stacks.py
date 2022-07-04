# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack():
    def __init__(self):
        self.stack = []
        
    def empty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.empty() is False:
            return self.stack.pop()
        
    def __str__(self):
        print(self.stack)
        
        
class Queue():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

        
    def enque(self, value):
        self.s1.push(value)
        self.s.append(value)
        
    def deque(self):
        if self.s1.empty() is False:
            while self.s1.empty() is False:
                self.s2.push(self.s1.pop())
            
            deque_result = self.s2.pop() if self.s2.empty() is False else 'Queue is empty'
            
            while self.s2.empty() is False:
                self.s1.push(self.s2.pop())
                
            return deque_result
        else:
            return 'Queue is empty'
        
    def front(self):
        if self.s1.empty() is False:
            while self.s1.empty() is False:
                self.s2.push(self.s1.pop())
                
            deque_result = self.s2.pop() if self.s2.empty() is False else 'Queue is empty'
            
            if deque_result != 'Queue is empty':
                self.s1.push(deque_result)
                
            while self.s2.empty() is False:
                self.s1.push(self.s2.pop())
                
            return deque_result
        else:
            return 'Queue is empty'
        
    def __str__(self):
        print(self.s1)
        

def get_queries(query_count):
    operations = []
    for _ in range(query_count):
        try:
            inp = input()
            if len(inp) == 1:
                ins = [int(inp), None]
                ins = tuple(ins)
            else:
                ins = inp.split()
                for pos in range(len(ins)):
                    ins[pos] = int(ins[pos])
                ins = tuple(ins)
                
            # append the instruction string as a tuple
            # after converting string numbers to integers
            operations.append(ins)
        except:
            break
    
    return operations

def resolve_queries(query_count, queries):
    q = Queue()
    for query in queries:
        if query[0] == 1: q.enque(query[1])
        if query[0] == 2: q.deque()
        if query[0] == 3: print(q.front())
    
if __name__ == '__main__':
    query_count = int(input())
    queries     = get_queries(query_count)
    resolve_queries(query_count, queries)

# Kunal Wadhwa

'''
Implement an interpreter for a language that maintains a single global stack of values and supports
the following instructions:
    push X:  push the argument X onto the stack; the argument is always an integer
    print:   pop an item off the stack and print it
    add:     pop the top two items, add them and push the result
    mul:     pop the top two items, multiply them and push the result
    sub:     pop the top two items, subtract them and push the result
    div:     pop the top two items, divide them and push the result
An example program:
input: ["push 2", "push 3", "push 4", "sub", "print"]
Instruction | Stack after evaluation | Output
============|========================|========
push 2      | [2]                    |
push 3      | [3,2]                  |
push 4      | [4,3,2]                |
sub         | [1,2]                  |
print       | [2]                    | 1


class Interpreter {
    public void evaluate(String[] instructions) {
    }
}
'''

class stack:
    def __init__(self):
        self.s = []

    # Push
    def push(self, value):
        self.s.append(value)
        return

    # Print
    def stack_print(self):
        try:
            print(self.s.pop())
        except:
            raise Exception('Not enough elements in the stack.')
    
    # Pop
    def pop(self):
        try:
            return self.s.pop()
        except:
            raise Exception('Not enough elements in the stack.')

    # Add
    def add(self):
        try:
            self.push(self.pop() + self.pop())
            return
        except:
            raise Exception('Not enough elements in the stack.')

    # Multiply
    def mul(self):
        try:
            self.push(self.pop() * self.pop())
            return
        except:
            raise Exception('Not enough elements in the stack.')


    # Subtract
    def sub(self):
        try:
            self.push(self.pop() - self.pop())
            return
        except:
            raise Exception('Not enough elements in the stack.')

    # Divide
    def div(self):
        try:
            self.push(self.pop() / self.pop())
            return
        except:
            raise Exception('Not enough elements in the stack.')
    
    # Testing: Get stack
    def get(self):
        print(self.s)



def evaluate(instructions):
    s = stack()
    
    for instruction in instructions:
        if 'push' in instruction:
            push_value = int(instruction.strip('push '))
            s.push(push_value)
        elif 'print' in instruction:
            s.stack_print()
        elif 'add' in instruction:
            s.add()
        elif 'mul' in instruction:
            s.mul()
        elif 'sub' in instruction:
            s.sub()
        elif 'div' in instruction:
            s.div()


if __name__ == '__main__':
    instructions = ["push 2", "push 3", "push 4", "sub", "print"]
    evaluate(instructions)

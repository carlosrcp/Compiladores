# o arquivo Calc1.stk é input do compilador
class RPNStacker:
    def __init__(self):
        self.stack = []
        self.inputs = []

    def start(self):
        with open('Calc1.stk', 'r') as f:
            self.inputs = f.read().split()

        print(self.inputs)
        while(len(self.inputs)>0):
            if self.inputs[0].isdigit():
                self.stack.append(int(self.inputs.pop(0)))
            elif len(self.stack) >= 2:
                op2 = self.stack.pop()                
                op1 = self.stack.pop()
                operator = self.inputs.pop(0)
                if operator == '+':
                    self.stack.append(op1+op2)
                elif operator == '-':
                    self.stack.append(op1-op2)
                elif operator == '*':
                    self.stack.append(op1*op2)
                elif operator == '/':
                    self.stack.append(op1/op2)
            else :
                print("erro!")
                return
        
        print(self.stack[0])


comp = RPNStacker()

comp.start()
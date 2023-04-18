# o arquivo Calc1.stk é input do compilador
from enum import Enum

printTokens = True

class TokenType(Enum):
    NUM = 1
    PLUS = 2
    MINUS = 3
    SLASH = 4
    STAR = 5
    EOF = 6

class Token():
    def __init__(self, tokenType, lexeme) -> None:
        self.tokenType = tokenType
        self.lexeme = lexeme
    
    def str(self):
        return f'Token [type={self.tokenType}, lexeme={self.lexeme}]'

validOps = ['+','-','/','*']

class RPNStacker:
    def __init__(self):
        self.stack = []
        self.inputs = []

    def start(self):
        # leitura do arquivo
        with open('Calc1.stk', 'r') as f:
            self.inputs = f.read().split()
        
        # transformacao em tokens
        for i in range(len(self.inputs)):
            if self.inputs[i].isdigit():
                self.inputs[i] = Token(TokenType.NUM, self.inputs[i])
            elif self.inputs[i] == '+':
                self.inputs[i] = Token(TokenType.PLUS, self.inputs[i])
            elif self.inputs[i] == '-':
                self.inputs[i] = Token(TokenType.MINUS, self.inputs[i])
            elif self.inputs[i] == '/':
                self.inputs[i] = Token(TokenType.SLASH, self.inputs[i])
            elif self.inputs[i] == '*':
                self.inputs[i] = Token(TokenType.STAR, self.inputs[i])
            else:
                return print(f'Error: Unexpected character: {self.inputs[i]}')
        
        self.inputs.append(Token(TokenType.EOF, 'EOF'))
        
        #print dos tokens
        if printTokens:
            for i in self.inputs:
                print(f'Token [type={i.tokenType.name}, lexeme={i.lexeme}]')
            
        # leitura dos tokens
        while(self.inputs[0].tokenType!=TokenType.EOF):             
            if self.inputs[0].tokenType == TokenType.NUM:
                self.stack.append(self.inputs.pop(0).lexeme)
            elif len(self.stack) >= 2:
                    op2 = float(self.stack.pop())                
                    op1 = float(self.stack.pop())
                    operator = self.inputs.pop(0).tokenType

                    if operator == TokenType.PLUS:
                        self.stack.append(op1+op2)
                    elif operator == TokenType.MINUS:
                        self.stack.append(op1-op2)
                    elif operator == TokenType.STAR:
                        self.stack.append(op1*op2)
                    elif operator == TokenType.SLASH:
                        self.stack.append(op1/op2)
            else:
                return print("Error: operacao impossivel")
        
        print(f'Saida: {self.stack[0]}')


comp = RPNStacker()

comp.start()
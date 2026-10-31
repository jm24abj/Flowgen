import Helpers

print("Parser.py loaded")

tokens = []
tokenPosition = 0

class Parser:

    def __init__(self, tokenStream):
        self.tokens = tokenStream
        self.token = None
        self.tokenPosition = 0
        self.ast = []

    def parse(self):
        while self.tokenPosition < len(self.tokens):
            node = self.program()
            if node is not None:
                self.ast.append(node)

    def program(self):
        self.token = self.next()

        match self.token.tokenType:
            case Helpers.TokenType.FUNCTION:
                self.func()
            case Helpers.TokenType.IF:
                self.decision()
            case Helpers.TokenType.WHILE:
                self.whileloop()
            case Helpers.TokenType.BRANCH:
                self.branch()
            case Helpers.TokenType.LABEL:
                self.func()
            case Helpers.TokenType.TITLE:
                self.title()
            case Helpers.TokenType.STATEMENT:
                self.statement()

    def func(self):
        pass

    def decision(self):
        pass

    def whileloop(self):
        pass

    def branch(self):
        pass

    def label(self):
        pass

    def title(self):
        pass

    def statement(self):
        pass
    
    def next(self):
        if self.tokenPosition < len(self.tokens):
            self.token = self.tokens[self.tokenPosition]
            print(f"Parser: Consuming token: {self.token}")
            self.tokenPosition += 1

    def peekNext(self):
        if self.tokenPosition+1 < len(self.tokens):
            return self.tokens[self.tokenPosition+1]
        else:
            return None
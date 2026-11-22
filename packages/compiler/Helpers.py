from enum import Enum

print("Helpers.py loaded")

class TokenType(Enum):
    TITLE = "title" 
    WHITESPACE = ""
    STATEMENT = "Statement"
    SEMICOLON = ";"
    LBRACE = "{"
    RBRACE = "}"
    LPAREN = "("
    RPAREN = ")"
    ASSIGN = "="
    IF = "if"
    ELIF = "elif"
    ELSE = "else"
    WHILE = "while"
    OPTIONS = "options"
    LABEL = ":" 
    FOR = "for"
    FUNCTION = "function"
    IO = "IO" 

class FlowchartSymbol(Enum):
    PROGRAM = "PROGRAM"
    START = "START"
    END = "END"
    PROCESS = "PROCESS"
    DECISION = "DECISION"
    INPUT_OUTPUT = "IO"
    CONNECTOR = "CONNECTOR"

class Token:

    def __init__(self, tokenType: TokenType, line: int, lexeme: str = None):
        self.tokenType = tokenType
        self.lexeme = lexeme if lexeme is not None else tokenType.value # incase a string token is made as it could be anything
        self.line = line

    def __str__(self):
        return f"Token(type={self.tokenType}, value='{self.lexeme}', line={self.line})"

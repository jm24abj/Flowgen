from enum import Enum

print("Helpers.py loaded")

class TokenType(Enum):
    TITLE = "title" # OPTIONAL EXPORT TITLE FOR FLOWCHART
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
    BRANCH = "branch"
    LABEL = ":" 
    LOOP = "loop"
    FUNCTION = "function"

class FlowchartSymbol(Enum):
    PROGRAM = "PROGRAM"
    START = "START"
    END = "END"
    PROCESS = "PROCESS"
    DECISION = "DECISION"
    INPUT_OUTPUT = "IO"
    CONNECTOR = "CONNECTOR"

class FlowNode:

    def __init__(self, symbol: FlowchartSymbol, text: str):
        self.symbol = symbol
        self.text = text
        self.previous = []  # List of previous nodes (for branching) in the format [(FlowNode, true), (FlowNode, false), (FlowNode, condition), ...]
        self.next = []  # List of next nodes (for branching) in the format [(FlowNode, true), (FlowNode, false), (FlowNode, condition), ...]

    def add_next_node(self, node, condition=None):
        self.next.append((node, condition))

    def add_previous_node(self, node, condition=None):
        self.previous.append((node, condition))

class Token:

    def __init__(self, tokenType: TokenType, line: int, lexeme: str = None):
        self.tokenType = tokenType
        self.lexeme = lexeme if lexeme is not None else tokenType.value # incase a string token is made as it could be anything
        self.line = line

    def __str__(self):
        return f"Token(type={self.tokenType}, value='{self.lexeme}', line={self.line})"

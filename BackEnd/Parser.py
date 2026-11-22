import Helpers

print("Parser.py loaded")

class ParserError(Exception):
    pass

class Parser:

    def __init__(self, tokenStream):
        self.tokens = tokenStream
        self.tokenPosition = 0
        self.ast = []
        self.errorLog = []

    # For more information on the grammar, see the documentation in the README.md file which contains the EBNF grammar rules.

    # Program = Title, {Process | Function | ControlFlowStatement};
    def parse(self):
        try:
            self.ast.append(self.title())

            while self.tokenPosition < len(self.tokens):
                node = self.programItem()
                self.ast.append(node)

        except ParserError as error:
            self.errorLog.append(str(error))
            print(f"Parser Error: {error}")

        return self.ast

    # Program = Title, {Process | Function | ControlFlowStatement};
    def programItem(self):
        if self.check("FUNCTION"):
            return self.func()

        elif self.check("STATEMENT"):
            return self.process()

        elif self.check("IF", "WHILE", "FOR", "OPTIONS", "IO"):
            return self.controlFlowStatement()

        else:
            self.error("Expected a Process, Function or ControlFlowStatement")

    # Title = "title", "=", Process;
    def title(self):
        self.expect("TITLE")
        self.expect("=")

        node = self.process()

        return {
            "type": "Title",
            "value": node
        }

    # Process = Statement, ";";
    def process(self):
        statement = self.statement()
        self.expect(";")

        return {
            "type": "Process",
            "statement": statement
        }

    # Statement = ValidCharacter, {ValidCharacter | Digit};
    def statement(self):
        token = self.expect("STATEMENT")

        return {
            "type": "Statement",
            "value": self.tokenValue(token)
        }

    # Function = "function", ":", Statement, Block;
    def func(self):
        self.expect("FUNCTION")
        self.expect(":")

        name = self.statement()
        body = self.block()

        return {
            "type": "Function",
            "name": name,
            "body": body
        }

    # ControlFlowStatement = If | While | Loop | Options | IO;
    def controlFlowStatement(self):
        if self.check("IF"):
            return self.decision()

        elif self.check("WHILE"):
            return self.whileLoop()

        elif self.check("FOR"):
            return self.loop()

        elif self.check("OPTIONS"):
            return self.options()

        elif self.check("IO"):
            return self.io()

        else:
            self.error("Expected a ControlFlowStatement")

    # If = "if", "(", Statement, ")", Block, {Elif}, Else;
    def decision(self):
        self.expect("IF")
        self.expect("(")

        condition = self.statement()

        self.expect(")")

        body = self.block()
        elifNodes = []

        while self.check("ELIF"):
            elifNodes.append(self.elifStatement())

        elseNode = self.elseStatement()

        return {
            "type": "If",
            "condition": condition,
            "body": body,
            "elif": elifNodes,
            "else": elseNode
        }

    # Elif = "elif", "(", Statement, ")", Block;
    def elifStatement(self):
        self.expect("ELIF")
        self.expect("(")

        condition = self.statement()

        self.expect(")")

        body = self.block()

        return {
            "type": "Elif",
            "condition": condition,
            "body": body
        }

    # Else = "else", Block;
    def elseStatement(self):
        self.expect("ELSE")

        body = self.block()

        return {
            "type": "Else",
            "body": body
        }

    # While = "while", "(", Statement, ")", Block;
    def whileLoop(self):
        self.expect("WHILE")
        self.expect("(")

        condition = self.statement()

        self.expect(")")

        body = self.block()

        return {
            "type": "While",
            "condition": condition,
            "body": body
        }

    # Loop = "for", "(", Statement, ";", Statement, ";", Statement, ")", Block;
    def loop(self):
        self.expect("FOR")
        self.expect("(")

        initialisation = self.statement()
        self.expect(";")

        condition = self.statement()
        self.expect(";")

        increment = self.statement()
        self.expect(")")

        body = self.block()

        return {
            "type": "For",
            "initialisation": initialisation,
            "condition": condition,
            "increment": increment,
            "body": body
        }

    # Options = "options", "{", Option, {Option}, "}";
    def options(self):
        self.expect("OPTIONS")
        self.expect("{")

        options = []
        options.append(self.option())

        while not self.check("}"):
            if self.tokenPosition >= len(self.tokens):
                self.error("Expected '}' to close options")

            options.append(self.option())

        self.expect("}")

        return {
            "type": "Options",
            "options": options
        }

    # Option = Statement, Block;
    def option(self):
        name = self.statement()
        body = self.block()

        return {
            "type": "Option",
            "name": name,
            "body": body
        }

    # IO = "IO", "=", Process;
    def io(self):
        self.expect("IO")
        self.expect("=")

        process = self.process()

        return {
            "type": "IO",
            "process": process
        }

    # Block = "{", {Process | ControlFlowStatement}, "}";
    def block(self):
        self.expect("{")

        statements = []

        while not self.check("}"):
            if self.tokenPosition >= len(self.tokens):
                self.error("Expected '}' to close block")

            if self.check("STATEMENT"):
                statements.append(self.process())

            else:
                statements.append(self.controlFlowStatement())

        self.expect("}")

        return {
            "type": "Block",
            "statements": statements
        }

    def current(self):
        while self.tokenPosition < len(self.tokens):
            token = self.tokens[self.tokenPosition]

            if self.tokenKind(token) == "WHITESPACE":
                self.tokenPosition += 1
                continue

            return token

        return None
    
    def tokenKind(self, token):
        if token is None:
            return None

        kind = token.tokenType

        if hasattr(kind, "name"):
            return kind.name.upper()

        return str(kind).upper()

    def tokenValue(self, token):
        if token is None:
            return None

        for attribute in ("value", "lexeme", "tokenValue"):
            if hasattr(token, attribute):
                return str(getattr(token, attribute))

        return str(token.tokenType)

    def check(self, *expected):
        token = self.current()

        if token is None:
            return False

        kind = self.tokenKind(token)
        value = self.tokenValue(token)

        for item in expected:
            item = item.upper()

            if kind == item:
                return True

            if value == item or value.upper() == item:
                return True

        return False

    def next(self):
        token = self.current()

        if token is not None:
            #print(f"Parser: Consuming token: {token}")
            self.tokenPosition += 1

        return token
    
    def expect(self, expected):
        if not self.check(expected):
            self.error(
                f"Expected '{expected}', got '{self.current()}'"
            )

        return self.next()

    def peekNext(self):
        position = self.tokenPosition + 1

        if position < len(self.tokens):
            return self.tokens[position]

        return None

    def error(self, message):
        token = self.current()

        if token is None:
            raise ParserError(
                f"Syntax error at end of input: {message}"
            )

        raise ParserError(
            f"Syntax error at token {self.tokenPosition}: "
            f"{message}. Got {token}"
        )

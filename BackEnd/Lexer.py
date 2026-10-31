import Helpers

print("Lexer.py loaded")

def lexer(source_code):

    tokens = []
    lineNumber = 1
    stringBuilder = ""

    for char in source_code:

        tokenSize = len(tokens)

        if char == '\n':
            lineNumber += 1
            stringBuilder = ""
        elif char == ';':
            tokens.append(determineTokenType(stringBuilder.strip(), lineNumber))
            tokens.append(Helpers.Token(Helpers.TokenType.SEMICOLON, lineNumber))
        elif char == '{':
            tokens.append(determineTokenType(stringBuilder.strip(), lineNumber))
            tokens.append(Helpers.Token(Helpers.TokenType.LBRACE, lineNumber))
        elif char == '}':
            tokens.append(determineTokenType(stringBuilder.strip(), lineNumber))
            tokens.append(Helpers.Token(Helpers.TokenType.RBRACE, lineNumber))
        elif char == '(':
            tokens.append(determineTokenType(stringBuilder.strip(), lineNumber))
            tokens.append(Helpers.Token(Helpers.TokenType.LPAREN, lineNumber))
        elif char == ')':
            tokens.append(determineTokenType(stringBuilder.strip(), lineNumber))
            tokens.append(Helpers.Token(Helpers.TokenType.RPAREN, lineNumber))
        elif char == '=':
            tokens.append(determineTokenType(stringBuilder.strip(), lineNumber))
            tokens.append(Helpers.Token(Helpers.TokenType.ASSIGN, lineNumber))
        elif char == ':':
            tokens.append(determineTokenType(stringBuilder.strip(), lineNumber))
            tokens.append(Helpers.Token(Helpers.TokenType.LABEL, lineNumber))
        else:
            stringBuilder += char

        if len(tokens) != tokenSize:
            stringBuilder = ""

    return tokens

def determineTokenType(token, lineNumber): # helps multi character tokens like "if" or "while" to be recognized as their own token type instead of a statement

    if token == "if":
        return Helpers.Token(Helpers.TokenType.IF, lineNumber)
    elif token == "elif":
        return Helpers.Token(Helpers.TokenType.ELIF, lineNumber)
    elif token == "else":
        return Helpers.Token(Helpers.TokenType.ELSE, lineNumber)
    elif token == "while":
        return Helpers.Token(Helpers.TokenType.WHILE, lineNumber)
    elif token == "branch":
        return Helpers.Token(Helpers.TokenType.BRANCH, lineNumber)
    elif token == ":":
        return Helpers.Token(Helpers.TokenType.LABEL, lineNumber)
    elif token == "loop":
        return Helpers.Token(Helpers.TokenType.LOOP, lineNumber)
    elif token == "function":
        return Helpers.Token(Helpers.TokenType.FUNCTION, lineNumber)
    elif token == "title":
        return Helpers.Token(Helpers.TokenType.TITLE, lineNumber)
    elif token == "":
        return Helpers.Token(Helpers.TokenType.WHITESPACE, lineNumber)
    else:
        return Helpers.Token(Helpers.TokenType.STATEMENT, lineNumber, token)
    
class CompilationError:

    def __init__(self,lineNumber):
        self.lineNumber = lineNumber

    def __str__(self):
        return f"Error on line {self.lineNumber}. error cannot be determined please re-read and try again."

class UnexpectedTokenError(CompilationError):
    def __init__(self, lineNumber, missingToken):
        super().__init__(lineNumber)
        self.missingToken = missingToken

    def __str__(self):
        return f"Expected {self.missingToken} on line {self.lineNumber}"

class GrammarViolationError(CompilationError):
    def __init__(self, lineNumber,tokenGiven,expectedTokens):
        super().__init__(lineNumber)
        self.tokenGiven = tokenGiven
        self.expectedTokens = expectedTokens

    def __str__(self):
        return f"{self.tokenGiven} on line {self.lineNumber} doesn't match expected grammer. Expected one of the following {self.expectedTokens}"
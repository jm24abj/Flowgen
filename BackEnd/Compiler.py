import Lexer
import Parser

print("Compiler.py loaded")

def compile(file_path):

    # Gather the source code from the file

    file = open(file_path, "r")
    sourceCode = file.read()
    file.close()

    # Tokenize the source code using the lexer

    tokens = Lexer.lexer(sourceCode)
    ast = Parser.Parser(tokens).parse()

if __name__ == "__main__":
    compile("BackEnd/test.txt")
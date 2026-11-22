import Lexer as Lexer
import Parser as Parser
import ASTPrinter as ASTPrinter

def compile(file_path):

    # Gather the source code from the file

    file = open(file_path, "r")
    sourceCode = file.read()
    file.close()

    # Tokenize the source code using the lexer

    tokens = Lexer.lexer(sourceCode)
    ast = Parser.Parser(tokens).parse()

    printer = ASTPrinter.AstPrinter()
    printer.printAst(ast)

if __name__ == "__main__":
    compile("Tests/test.txt")
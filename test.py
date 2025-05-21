from antlr4 import *
from Gramatyka.KonturLexer import KonturLexer
from Gramatyka.KonturParser import KonturParser
from Gramatyka.interpreter import KonturInterpreter

def main():
    code = """
int i = 1;
if(true){
    display(i);
}
    """

    input_stream = InputStream(code)
    lexer = KonturLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = KonturParser(tokens)

    tree = parser.program()
    visitor = KonturInterpreter()
    visitor.visit(tree)
    print(visitor.variables)
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
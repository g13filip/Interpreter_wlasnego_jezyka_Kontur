from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.FileStream import FileStream
from antlr4.tree.Tree import TerminalNodeImpl

from KonturLexer import KonturLexer
from KonturParser import KonturParser

def print_tree(node, parser, indent=0):
    prefix = "  " * indent
    if isinstance(node, TerminalNodeImpl):
        print(f"{prefix}{node.getText()}")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print(f"{prefix}{rule_name}")
        for child in node.getChildren():
            print_tree(child, parser, indent + 5)

def parse_kontur_file(file_path):
    input_stream = FileStream(file_path)
    lexer = KonturLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = KonturParser(stream)

    tree = parser.program()

    print_tree(tree, parser)

    return tree

if __name__ == "__main__":

    parse_kontur_file("plik.txt")
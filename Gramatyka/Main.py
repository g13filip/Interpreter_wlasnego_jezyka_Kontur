import sys
from antlr4 import *
from KonturLexer import KonturLexer
from KonturParser import KonturParser
from antlr4.tree.Trees import Trees

def parse_kontur_file(file_path):
    input_stream = FileStream(file_path)
    lexer = KonturLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = KonturParser(stream)

    tree = parser.program()  # Główna reguła gramatyki

    # Wydrukuj drzewo składniowe (tekstowo)
    print(Trees.toStringTree(tree, None, parser))

    return tree

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python parse_kontur.py <ścieżka_do_pliku>")
        sys.exit(1)

    parse_kontur_file(sys.argv[1])
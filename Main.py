from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.FileStream import FileStream
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import TerminalNodeImpl
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from Gramatyka.KonturErrorListener import KonturErrorListener
from Gramatyka.KonturLexer import KonturLexer
from Gramatyka.KonturParser import KonturParser

# def print_tree(node, parser, indent=0):
#     prefix = "  " * indent
#     if isinstance(node, TerminalNodeImpl):
#         print(f"{prefix}{node.getText()}")
#     else:
#         rule_name = parser.ruleNames[node.getRuleIndex()]
#         print(f"{prefix}{rule_name}")
#         for child in node.getChildren():
#             print_tree(child, parser, indent + 3)
#
# def parse_kontur_file(input):
#     # input_stream = FileStream(file_path)
#     lexer = KonturLexer(input)
#     stream = CommonTokenStream(lexer)
#     parser = KonturParser(stream)
#
#     tree = parser.program()
#
#     print_tree(tree, parser)
#
#     return tree

def print_tree(node, parser, indent=0):
    result = []
    prefix = "  " * indent

    if isinstance(node, TerminalNodeImpl):
        result.append(f"{prefix}{node.getText()}")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        result.append(f"{prefix}{rule_name}")
        for child in node.getChildren():
            result.append(print_tree(child, parser, indent + 1) + '\n')

    return "".join(filter(None, result))


def parse_kontur_file(input_text):

    input_stream = InputStream(input_text)
    lexer = KonturLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = KonturParser(stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    error_listener = KonturErrorListener()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()
    tree_text = print_tree(tree, parser)

    return tree, tree_text, error_listener.errors

if __name__ == "__main__":

    st.title("Interpreter języka Kontur")

    expression = st.text_area("Wprowadź wyrażenie do obliczenia:","", height = 300)

    if st.button("Analizuj"):
        if not expression.strip():
            st.warning("Proszę wprowadzić wyrażenie")
        else:
            try:
                tree, tree_text, errors = parse_kontur_file(expression)

                if errors:
                    st.subheader("Błędy:")
                    for error in errors:
                        st.error(error)
                else:
                    st.subheader("Wynik \\ Drzewo składniowe:")
                    st.code(tree_text, language='text')

            except Exception as e:
                st.error(f"Krytyczny błąd przetwarzania: {str(e)}")
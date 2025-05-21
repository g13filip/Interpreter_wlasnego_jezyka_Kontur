import streamlit as st
from antlr4 import *
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from Gramatyka.KonturErrorListener import KonturErrorListener
from Gramatyka.KonturLexer import KonturLexer
from Gramatyka.KonturParser import KonturParser
from Gramatyka.interpreter import KonturInterpreter

# Tekstowe pole do wprowadzenia kodu
st.title("Interpreter języka Kontur")
code = st.text_area("Wprowadź wyrażenie do obliczenia:","", height = 300)

# Przycisk uruchamiający interpreter
if st.button("Uruchom kod"):
    if not code.strip():
        st.warning("Proszę wprowadzić wyrażenie")
    try:

        input_stream = InputStream(code)
        lexer = KonturLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = KonturParser(token_stream)

        lexer.removeErrorListeners()
        parser.removeErrorListeners()

        error_listener = KonturErrorListener()
        lexer.addErrorListener(error_listener)
        parser.addErrorListener(error_listener)

        tree = parser.program()

        if error_listener.errors:
            st.subheader("Błędy:")
            for error in error_listener.errors:
                st.error(error)
        else:
            st.subheader("Wynik programu:")
            interpreter = KonturInterpreter(output_func=st.write)
            interpreter.visit(tree)



    except Exception as e:
        st.error(f"Błąd: {e}")
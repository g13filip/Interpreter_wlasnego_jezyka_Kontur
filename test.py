# import streamlit as st
# from antlr4 import *
# from antlr4.CommonTokenStream import CommonTokenStream
# from antlr4.InputStream import InputStream
# from streamlit_ace import st_ace
#
# from Gramatyka.KonturErrorListener import KonturErrorListener
# from Gramatyka.KonturLexer import KonturLexer
# from Gramatyka.KonturParser import KonturParser
# from Gramatyka.interpreter import KonturInterpreter
#
#
# st.title("Interpreter języka Kontur")
#
# code = st_ace(
#     value="",
#     placeholder="Wprowadź wyrażenie do obliczenia",
#     language="text",
#     theme="dracula",
#     keybinding="vscode",
#     font_size=14,
#     tab_size=4,
#     show_gutter=True,
#     show_print_margin=True,
#     wrap=False,
#     auto_update=False,
#     height="300px",
#     key="ace-editor"
# )
#
# if st.button("Uruchom kod"):
#     if not code.strip():
#         st.warning("Proszę wprowadzić wyrażenie")
#     try:
#         input_stream = InputStream(code)
#         lexer = KonturLexer(input_stream)
#         token_stream = CommonTokenStream(lexer)
#         parser = KonturParser(token_stream)
#
#         lexer.removeErrorListeners()
#         parser.removeErrorListeners()
#
#         error_listener = KonturErrorListener()
#         lexer.addErrorListener(error_listener)
#         parser.addErrorListener(error_listener)
#
#         tree = parser.program()
#         # print(tree.toStringTree(recog=parser))
#         if error_listener.errors:
#             st.subheader("Błędy:")
#             for error in error_listener.errors:
#                 st.error(error)
#         else:
#             st.subheader("Wynik programu:")
#             interpreter = KonturInterpreter(output_func=st.write)
#             interpreter.visit(tree)
#             print(interpreter.variables)
#
#     except Exception as e:
#         st.error(f"Błąd: {e}")
import sys

import streamlit as st
import plotly.graph_objects as go  # ZMIANA: Potrzebujemy tego importu
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from Gramatyka.KonturLexer import KonturLexer
from Gramatyka.KonturParser import KonturParser
from Gramatyka.interpreter import KonturInterpreter
from Gramatyka.KonturErrorListener import KonturErrorListener
from streamlit_ace import st_ace

st.title("Interpreter języka Kontur")

code = st_ace(
    value="",
    placeholder="Wprowadź wyrażenie do obliczenia",
    language="text",
    theme="dracula",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    show_gutter=True,
    show_print_margin=True,
    wrap=False,
    auto_update=False,
    height="300px",
    key="ace-editor"
)

if st.button("Uruchom kod"):
    if not code.strip():
        st.warning("Proszę wprowadzić wyrażenie")
        st.stop()  # Zatrzymujemy wykonanie, jeśli nie ma kodu
    flag = False
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
            st.subheader("Błędy parsowania:")
            for error in error_listener.errors:
                st.error(error)
            flag = True
        else:
            interpreter = KonturInterpreter(output_func=st.write)
            interpreter.visit(tree)

    except Exception as e:
        st.error(f"Błąd: {e}")
    finally:
        if not flag and interpreter:
            if interpreter.results:
                st.subheader("Wygenerowane wyniki:")
                for result in interpreter.results:
                    if isinstance(result, go.Figure):
                        st.plotly_chart(result, use_container_width=True)
                    else:
                        st.write(result)
            else:
                st.info("Program wykonany pomyślnie, ale nie wygenerował żadnych graficznych wyników (plot/display).")

import streamlit as st
from antlr4 import *
from Gramatyka.KonturLexer import KonturLexer
from Gramatyka.KonturParser import KonturParser
from Gramatyka.interpreter import KonturInterpreter

# Tekstowe pole do wprowadzenia kodu
st.title("Interpreter języka Kontur")
code = st.text_area("Wklej kod Kontur:", '''int i = 0;
while (i < 10) {
    if (i % 2 == 0) {
        display(i);
    }
    i += 1;
}''', height=300)

# Przycisk uruchamiający interpreter
if st.button("Uruchom kod"):
    try:
        # Przetwarzanie kodu źródłowego
        input_stream = InputStream(code)
        lexer = KonturLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = KonturParser(token_stream)
        tree = parser.program()

        st.subheader("Wynik programu:")

        # Tworzymy interpreter z funkcją wyjściową: st.write
        interpreter = KonturInterpreter(output_func=st.write)
        interpreter.visit(tree)

    except Exception as e:
        st.error(f"Błąd: {e}")
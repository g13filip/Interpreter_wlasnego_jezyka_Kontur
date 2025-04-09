# from Kolorowanie import tokens_to_html
# from Scaner import scan
#
# tokens = []
# file = open("Polecenia.txt", "r")
#
# for line in file:
#     i = 0
#     text = line
#     temp = []
#     while i < len(text):
#         try:
#             token , i = scan(text,i)
#             temp.append(token)
#         except Exception as e:
#             print(e)
#             exit(8)
#     tokens.append(temp)
#
# tokens_to_html(tokens)

# import tkinter as tk
# import sys
# import io
#
# def interpretuj():
#     kod = pole_tekstowe.get("1.0", tk.END)
#
#     # Przechwyć standardowe wyjście (stdout)
#     stary_stdout = sys.stdout
#     sys.stdout = io.StringIO()
#
#     try:
#         exec(kod, {})  # wykonaj cały kod
#         wynik = sys.stdout.getvalue()  # pobierz to, co zostało wypisane przez print()
#         okno_wyniku.config(state='normal')       # pozwól edytować pole
#         okno_wyniku.delete("1.0", tk.END)         # wyczyść stare dane
#         okno_wyniku.insert(tk.END, wynik)         # wstaw nowe
#         okno_wyniku.config(state='disabled')      # zablokuj ponownie (tylko do odczytu)
#     except Exception as e:
#         okno_wyniku.config(state='normal')
#         okno_wyniku.delete("1.0", tk.END)
#         okno_wyniku.insert(tk.END, f"Błąd: {e}")
#         okno_wyniku.config(state='disabled')
#     finally:
#         sys.stdout = stary_stdout  # przywróć stdout
#
# # Tworzymy GUI
# okno = tk.Tk()
# okno.title("Interpreter Python w Tkinterze")
#
# # Pole do wpisywania kodu
# pole_tekstowe = tk.Text(okno, height=10, width=60)
# pole_tekstowe.pack(pady=10)
#
# # Przycisk
# przycisk = tk.Button(okno, text="Wykonaj kod", command=interpretuj)
# przycisk.pack(pady=5)
#
# # Pole wynikowe
# okno_wyniku = tk.Text(okno, height=10, width=60, state='disabled', bg="#f0f0f0")
# okno_wyniku.pack(pady=10)
#
# okno.mainloop()

import sys
from antlr4 import *
from KonturLexer import KonturLexer
from KonturParser import KonturParser
from KonturListener import KonturListener

class MatlabListener(KonturListener):
    def enterExpression(self, ctx):
        print(f"Przetwarzam wyrażenie: {ctx.getText()}")

def main():
    input_stream = InputStream(input())
    lexer = KonturLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = KonturParser(stream)

    tree = parser.program()
    listener = MatlabListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
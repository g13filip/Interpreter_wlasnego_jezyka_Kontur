from Kolorowanie import tokens_to_html
from Scaner import scan

tokens = []
file = open("Polecenia.txt", "r")

for line in file:
    i = 0
    text = line
    temp = []
    while i < len(text):
        try:
            token , i = scan(text,i)
            temp.append(token)
        except Exception as e:
            print(e)
            exit(8)
    tokens.append(temp)

tokens_to_html(tokens)

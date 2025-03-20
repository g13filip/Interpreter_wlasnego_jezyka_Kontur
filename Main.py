from Scaner import scan, check_token_sequence, is_correct_bracketing
from Tokens import Token


text = "2+3*(76+8/3)+ 3*(9-3)"
i = 0
tokens = []
while i < len(text):
    try:
        token , i = scan(text,i)
        tokens.append(token)
    except Exception as e:
        print(e)
        exit(8)

try:
    check_token_sequence(tokens)
except Exception as e:
    print(e)
    exit(9)

for i in tokens:
    print(i)
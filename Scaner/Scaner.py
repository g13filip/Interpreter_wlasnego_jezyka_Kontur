from Errors import InvalidCharacter
from Tokens import Token

KEYWORDS = ["break", "if", "else", "for", "do", "while", "return","struct","class", "public", "private","print","def"]
CHARS = [";", ":", ","," ", "\t", "\n", "\""]
OPERATORS = ["=", "!", "+", "-", "*", "/", "<", ">"]
PARENTHESIS = ["(", ")", "[", "]", "{", "}"]
TYPES = ["void", "string","int","double", "float", "bool", "char"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def scan(text, indx):
    token_type = None
    temp = indx + 1
    char = text[indx]

    # Obsługa liczb (całkowitych i zmiennoprzecinkowych)
    if '0' <= char <= '9':
        token_type = 'Type_Number'
        isfloat = False
        char = text[temp] if temp < len(text) else ''

        while temp < len(text) and ('0' <= char <= '9' or char == '.'):
            if char == '.':
                if isfloat:
                    raise InvalidCharacter(f"Invalid character at column {temp}")
                isfloat = True
            temp += 1
            char = text[temp] if temp < len(text) else ''

    # Obsługa identyfikatorów
    elif ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_':
        token_type = 'Type_Identifier'
        char = text[temp] if temp < len(text) else ''
        while temp < len(text) and (
                ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or char == '_'):
            temp += 1
            char = text[temp] if temp < len(text) else ''

        if text[indx:temp] in KEYWORDS:
            token_type = 'Type_Keyword'
        if text[indx:temp] in TYPES:
            token_type = 'Type_Type'

    # Obsługa operatorów matematycznych
    elif char in OPERATORS:
        token_type = 'Type_Operator'

    # Obsługa nawiasów
    elif char in PARENTHESIS:
        token_type = 'Type_Parenthesis'

    elif char in CHARS:
        token_type = 'Type_Special'
    else:
        raise InvalidCharacter(f"Invalid character {char} at column {temp}")

    return Token(token_type, text[indx:temp], indx), temp
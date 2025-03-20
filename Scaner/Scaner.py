from Tokens import Token

class InvalidCharacter(Exception):
    pass

def scan(text, indx):
    token_type = None
    temp = indx + 1
    char = text[indx]

    # Pomijanie białych znaków
    while char in [' ', '\t'] and temp < len(text):
        temp += 1
        char = text[temp]

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

    # Obsługa operatorów matematycznych
    elif char in ['+', '-', '/', '*', '=']:
        token_type = 'Type_Operator'

    # Obsługa nawiasów
    elif char in ['(', ')']:
        token_type = 'Type_Parenthesis'

    else:
        raise InvalidCharacter(f"Invalid character {char} at column {temp}")

    # Zwrócenie tokenu, uwzględniając indeksy
    if temp < len(text) and text[temp] in [' ', '\t']:
        return Token(token_type, text[indx:temp], indx), temp + 1
    else:
        return Token(token_type, text[indx:temp], indx), temp


# Funkcja sprawdzająca poprawność kolejności podawanych tokenów

def check_token_sequence(tokens):

    if tokens[0].type == 'Type_Operator' or tokens[0].value == ')':
        raise(
            f"Invalid character on column: {tokens[0].start_indx}"
        )
    previous_token = None

    for i,token in enumerate(tokens):
        n = len(tokens)
    # po identyfikatorze lub liczbie może być tylko operator lub ')'
        if (token.type == 'Type_Number' or token.type == 'Type_Identifier') and n - 1 > i:
            if tokens[i + 1].type != 'Type_Operator' and tokens[i + 1].value != ')':
                raise InvalidCharacter(
                    f"Invalid character on column: {tokens[i+1].start_indx}")

        elif previous_token and previous_token.type == 'Type_Operator':
            if token.type != 'Type_Number' and token.value != '(' and token.type != 'Type_Identifier':
                raise InvalidCharacter(
                    f"Invalid character on column: {token.start_indx}")

        elif previous_token and previous_token.value == '(':
            if token.type == 'Type_Operator' or token.value == ')':
                raise InvalidCharacter(
                    f"Invalid character on column: {token.start_indx}")

        elif previous_token and previous_token.value == ')':
            if token.type != 'Type_Operator':
                raise InvalidCharacter(
                    f"Invalid character on column: {token.start_indx}")

        previous_token = token

    if previous_token.type == 'Type_Operator':
        raise InvalidCharacter(
            f"Invalid character on column: {previous_token.start_indx}")


    temp = is_correct_bracketing(tokens)
    if temp != -1:
        raise InvalidCharacter(
            f"Invalid character on column: {temp}"
        )


def is_correct_bracketing(tokens):
    stack = []
    for token in tokens:
        if token.value == '(':
            stack.append(token)  # Dodaj otwierający nawias do stosu
        elif token.value == ')':
            if not stack:  # Brak otwierającego nawiasu dla tego zamykającego
                return token.start_indx
            stack.pop()

    if len(stack) == 0:
        return -1
    else:
        return stack[-1].start_indx


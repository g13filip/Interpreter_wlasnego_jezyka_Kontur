# Funkcja sprawdzająca poprawność kolejności podawanych tokenów

class InvalidCharacter(Exception):
    pass

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


#funckja sprawdzająca poprawność nawiasowania

def is_correct_bracketing(tokens):
    stack = []
    for token in tokens:
        if token.value == '(':
            stack.append(token)
        elif token.value == ')':
            if not stack:
                return token.start_indx
            stack.pop()

    if len(stack) == 0:
        return -1
    else:
        return stack[-1].start_indx
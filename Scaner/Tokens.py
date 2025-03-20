class Token:

    def __init__(self, token_type, token_value, start_indx):
        self.type = token_type
        self.value = token_value
        self.start_indx = start_indx

    def __str__(self):
        return f"{self.type}: '{self.value}'"

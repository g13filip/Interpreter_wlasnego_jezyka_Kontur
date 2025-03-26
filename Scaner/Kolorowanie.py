def tokens_to_html(tokens, output_file="output.html"):
    colors = {
        'Type_Number': 'blue',
        'Type_Identifier': 'black',
        'Type_Operator': 'red',
        'Type_Parenthesis': 'purple',
        'Type_Special': 'green',
        'Type_Keyword': 'orange',
        'Type_Type': 'khaki'
    }

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("<html><head><title>Tokenized Output</title></head><body>")
        file.write("<pre>")

        for line_tokens in tokens:
            for token in line_tokens:
                color = colors[token.type]
                file.write(f'<span style="color: {color};">{token.value}</span>')

        file.write("</pre>")
        file.write("</body></html>")
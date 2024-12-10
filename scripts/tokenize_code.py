import re

def tokenize_code(source_code):
    tokens = re.findall(r'\w+|[^\w\s]', source_code)
    return tokens

# Example Usage
with open("data/raw/matrix_mul.c") as f:
    code = f.read()
tokens = tokenize_code(code)
print(tokens)


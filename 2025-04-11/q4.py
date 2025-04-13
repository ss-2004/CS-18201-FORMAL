# Q4 Model and analyze a simple text parser using formal grammar and automata theory.

import re

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})"


class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        token_spec = [
            ('NUMBER', r'\d+'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULT', r'\*'),
            ('DIV', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]

        tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_spec)
        for mo in re.finditer(tok_regex, self.input_text):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                self.tokens.append(Token('NUMBER', int(value)))
            elif kind in ('PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN'):
                self.tokens.append(Token(kind, value))
            elif kind == 'SKIP':
                continue
            else:
                raise SyntaxError(f"Unexpected character: {value}")
        self.tokens.append(Token('EOF', None))


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, type_):
        if self.current().type == type_:
            self.pos += 1
        else:
            raise SyntaxError(f"Expected {type_}, got {self.current()}")

    # Grammar Rules
    def parse(self):
        result = self.E()
        if self.current().type != 'EOF':
            raise SyntaxError("Unexpected input after complete parsing.")
        return result

    def E(self):
        node = self.T()
        return self.E_prime(node)

    def E_prime(self, left):
        tok = self.current()
        if tok.type == 'PLUS':
            self.eat('PLUS')
            right = self.T()
            return self.E_prime(('Add', left, right))
        elif tok.type == 'MINUS':
            self.eat('MINUS')
            right = self.T()
            return self.E_prime(('Sub', left, right))
        return left  # ε

    def T(self):
        node = self.F()
        return self.T_prime(node)

    def T_prime(self, left):
        tok = self.current()
        if tok.type == 'MULT':
            self.eat('MULT')
            right = self.F()
            return self.T_prime(('Mul', left, right))
        elif tok.type == 'DIV':
            self.eat('DIV')
            right = self.F()
            return self.T_prime(('Div', left, right))
        return left  # ε

    def F(self):
        tok = self.current()
        if tok.type == 'NUMBER':
            self.eat('NUMBER')
            return ('Num', tok.value)
        elif tok.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.E()
            self.eat('RPAREN')
            return node
        else:
            raise SyntaxError(f"Unexpected token: {tok}")


def evaluate(ast):
    if ast[0] == 'Num':
        return ast[1]
    elif ast[0] == 'Add':
        return evaluate(ast[1]) + evaluate(ast[2])
    elif ast[0] == 'Sub':
        return evaluate(ast[1]) - evaluate(ast[2])
    elif ast[0] == 'Mul':
        return evaluate(ast[1]) * evaluate(ast[2])
    elif ast[0] == 'Div':
        return evaluate(ast[1]) / evaluate(ast[2])
    else:
        raise ValueError("Invalid AST")

if __name__ == "__main__":
    input_expr = "3 + 5 * (2 - 1)"
    print(f"Input Expression: {input_expr}")
    lexer = Lexer(input_expr)
    parser = Parser(lexer.tokens)
    ast = parser.parse()
    print("Parsed AST:", ast)
    print("Evaluation Result:", evaluate(ast))

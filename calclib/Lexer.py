import re

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
    def GetTokens(self):
        for tok in self.text:
            if re.match('[0-9]', tok):
                try:
                    if self.tokens[-1][0] == 'INT' or self.tokens[-1][0] == 'FLOAT':
                        self.tokens[-1][-1] += tok
                    elif self.tokens[-1][0] == 'POW':
                        self.tokens[-1][-1] += f'{tok}'
                    else:
                        self.tokens.append(['INT', tok])
                except:
                    self.tokens.append(['INT', tok])
            elif tok == '.':
                try:
                    if self.tokens[-1][0] == 'INT':
                        self.tokens[-1][0] = 'FLOAT'
                        self.tokens[-1][-1] += tok
                    elif self.tokens[-1][0] == 'POW':
                        self.tokens[-1][-1] += f'{tok}'
                    elif self.token[-1][0] == 'FLOAT':
                        # Raise some error
                        pass
                    else:
                        self.tokens.append(['FLOAT', '0.'])
                except:
                    self.tokens.append(['FLOAT', '0.'])
            elif tok == '^':
                self.tokens.append(['POW', ''])
            elif tok in '+-*/%':
                self.tokens.append(['OP', tok])
            elif tok == '(':
                self.tokens.append(['LPARENT', tok])
            elif tok == ')':
                self.tokens.append(['RPARENT', tok])
            elif tok == ' ':
                self.tokens.append(['WHITESPACE'])
        return self.tokens
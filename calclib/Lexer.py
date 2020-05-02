import re

class Lexer:
    def __init__(self, text):
        # initialize
        self.text = text
        self.tokens = []
    def GetTokens(self):
        # bắt đầu lấy tokens
        for tok in self.text:
            # thêm tokens nếu xuất hiện int
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
            # dấu '.' dùng để phát hiện float
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
            # tokens dùng cho số mũ
            elif tok == '^':
                self.tokens.append(['POW', ''])
            # cộng, trừ, nhân, chia...
            elif tok in '+-*/%':
                self.tokens.append(['OP', tok])
            elif tok == '(':
                self.tokens.append(['LPARENT', tok])
            elif tok == ')':
                self.tokens.append(['RPARENT', tok])
            # dấu cách
            elif tok == ' ':
                self.tokens.append(['WHITESPACE'])
        # trả về tokens
        return self.tokens
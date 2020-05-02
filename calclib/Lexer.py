import re

class Lexer:
    def __init__(self, text):
        # initialize
        self.text = text
        self.tokens = []
    def GetTokens(self):
        tok = ''
        # bắt đầu lấy tokens
        for char in self.text:
            tok += char
            # thêm tokens nếu xuất hiện int
            if re.match('[0-9]', tok):
                try:
                    if self.tokens[-1][0] == 'INT' or self.tokens[-1][0] == 'FLOAT':
                        self.tokens[-1][-1] += tok
                    elif self.tokens[-1][0] == 'POW':
                        self.tokens[-1][-1] += f'{tok}'
                    elif self.tokens[-1][0] == 'SQRT'  and not self.tokens[-1][-1].endswith(')'):
                        self.tokens[-1][-1] += tok
                    else:
                        self.tokens.append(['INT', tok])
                    tok = ''
                except:
                    self.tokens.append(['INT', tok])
                    tok = ''
            # dấu '.' dùng để phát hiện float
            elif tok == '.':
                try:
                    if self.tokens[-1][0] == 'INT':
                        self.tokens[-1][0] = 'FLOAT'
                        self.tokens[-1][-1] += tok
                    elif self.tokens[-1][0] == 'POW':
                        self.tokens[-1][-1] += f'{tok}'
                    elif self.tokens[-1][0] == 'SQRT'  and not self.tokens[-1][-1].endswith(')'):
                        self.tokens[-1][-1] += tok
                    elif self.token[-1][0] == 'FLOAT':
                        # Raise some error
                        pass
                    else:
                        self.tokens.append(['FLOAT', '0.'])
                    tok = ''
                except:
                    self.tokens.append(['FLOAT', '0.'])
                    tok = ''
            # tokens dùng cho số mũ
            elif tok == '^':
                self.tokens.append(['POW', ''])
                tok = ''
            # cộng, trừ, nhân, chia...
            elif tok in '+-*/%':
                if self.tokens[-1][0] == 'SQRT' and not self.tokens[-1][-1].endswith(')'):
                    self.tokens[-1][-1] += tok
                else:
                    self.tokens.append(['OP', tok])
                tok = ''
            elif tok == '(':
                if self.tokens[-1][0] == 'SQRT' and not self.tokens[-1][-1].endswith(')'):
                    self.tokens[-1][-1] += tok
                else:
                    self.tokens.append(['LPARENT', tok])
                tok = ''
            elif tok == ')':
                if self.tokens[-1][0] == 'SQRT' and not self.tokens[-1][-1].endswith(')'):
                    self.tokens[-1][-1] += tok
                else:
                    self.tokens.append(['RPARENT', tok])
                tok = ''
            # dùng cho hàm căn bậc 2
            elif tok == 'sqrt' or tok == 'SQRT':
                self.tokens.append(['SQRT', ''])
                tok = ''
            # dấu cách
            elif tok == ' ':
                self.tokens.append(['WHITESPACE'])
                tok = ''
        # trả về tokens
        return self.tokens
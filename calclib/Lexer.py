import re, math
from . import CalclibException

class Lexer:
    angle = 'degree' # Đơn vị đo góc là 'degree' là default
    def __init__(self):
        # initialize
        self.tokens = []
    def GetTokens(self, text):
        self.text = text
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
                    elif self.tokens[-1][0] == 'SQRT'  and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
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
                    elif self.tokens[-1][0] == 'SQRT'  and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                        self.tokens[-1][-1] += tok
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
                if self.tokens[-1][0] == 'SQRT' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                    self.tokens[-1][-1] += tok
                else:
                    self.tokens.append(['OP', tok])
                tok = ''
            elif tok == '(':
                if self.tokens[-1][0] == 'SQRT' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                    self.tokens[-1][-1] += tok
                else:
                    self.tokens.append(['LPARENT', tok])
                tok = ''
            elif tok == ')':
                if self.tokens[-1][0] == 'SQRT' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                    self.tokens[-1][-1] += tok
                    if self.tokens[-1][0] == 'SIN' or self.tokens[-1][0] == 'COS' or self.tokens[-1][0] == 'TAN':
                        if self.angle == 'degree':
                            self.tokens[-1][-1] = f'{(eval(self.tokens[-1][-1])*math.pi)/180}'
                        elif self.angle != 'radian':
                            raise CalclibException.AngleUnitError("no angle unit named ", unit=self.angle)
                else:
                    self.tokens.append(['RPARENT', tok])
                tok = ''
            # dùng cho hàm căn bậc 2
            elif tok == 'sqrt' or tok == 'SQRT':
                self.tokens.append(['SQRT', ''])
                tok = ''
            # dùng cho sin
            elif tok == 'sin' or tok == 'SIN':
                self.tokens.append(['SIN', ''])
                tok = ''
            # dùng cho cos
            elif tok == 'cos' or tok == 'COS':
                self.tokens.append(['COS', ''])
                tok = ''
            elif tok == 'tan' or tok == 'TAN':
                self.tokens.append(['TAN', ''])
                tok = ''
            # dấu cách
            elif tok == ' ':
                self.tokens.append(['WHITESPACE'])
                tok = ''
        # trả về tokens
        return self.tokens
import re, math, sys
from . import CalclibException

class Lexer:
    angle = 'degree' # Đơn vị đo góc là 'degree' là default
    def __init__(self):
        # initialize
        self.tokens = []
    def GetTokens(self, text):
        if self.angle != 'degree' and self.angle != 'radian':
            raise CalclibException.AngleUnitError(f"no angle unit named '{self.angle}'")
        self.text = text
        self.tok = ''
        # bắt đầu lấy self.tokens
        for char in self.text:
            self.tok += char
            # thêm self.tokens nếu xuất hiện int
            if re.match('[0-9]', self.tok):
                try:
                    if self.tokens[-1][0] == 'INT' or self.tokens[-1][0] == 'FLOAT':
                        self.tokens[-1][-1] += self.tok
                    elif self.tokens[-1][0] == 'POW':
                        self.tokens[-1][-1] += f'{self.tok}'
                    elif self.tokens[-1][0][-4:] == 'SQRT'  and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                        self.tokens[-1][-1] += self.tok
                    else:
                        self.tokens.append(['INT', self.tok])
                    self.tok = ''
                except:
                    self.tokens.append(['INT', self.tok])
                    self.tok = ''
            # dấu '.' dùng để phát hiện float
            elif self.tok == '.':
                try:
                    if self.tokens[-1][0] == 'INT':
                        self.tokens[-1][0] = 'FLOAT'
                        self.tokens[-1][-1] += self.tok
                    elif self.tokens[-1][0] == 'POW':
                        self.tokens[-1][-1] += f'{self.tok}'
                    elif self.tokens[-1][0][-4:] == 'SQRT'  and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                        self.tokens[-1][-1] += self.tok
                    else:
                        self.tokens.append(['FLOAT', '.'])
                    self.tok = ''
                except:
                    self.tokens.append(['FLOAT', '.'])
                    self.tok = ''
            # self.tokens dùng cho số mũ
            elif self.tok == '^':
                self.tokens.append(['POW', ''])
                self.tok = ''
            # cộng, trừ, nhân, chia...
            elif self.tok in '+-*/%':
                if self.tokens[-1][0][-4:] == 'SQRT' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                    self.tokens[-1][-1] += self.tok
                else:
                    self.tokens.append(['OP', self.tok])
                self.tok = ''
            elif self.tok == '(' or self.tok == '[' or self.tok == '{':
                self.__checkBeginBuiltin()
                self.tok = ''
            elif self.tok == ')' or self.tok == ']' or self.tok == '}':
                self.__checkEndBuiltin()
                self.tok = ''
            # dùng cho hàm căn bậc 2
            elif self.tok == 'sqrt' or self.tok == 'SQRT':
                if self.tokens[-1][0] == 'INT':
                    self.tokens.append([f'{self.tokens[-1][-1]}SQRT', ''])
                    self.tokens.pop(-2)
                else:
                    self.tokens.append(['SQRT', ''])
                self.tok = ''
            # dùng cho sin
            elif self.tok == 'sin' or self.tok == 'SIN':
                self.tokens.append(['SIN', ''])
                self.tok = ''
            # dùng cho cos
            elif self.tok == 'cos' or self.tok == 'COS':
                self.tokens.append(['COS', ''])
                self.tok = ''
            elif self.tok == 'tan' or self.tok == 'TAN':
                self.tokens.append(['TAN', ''])
                self.tok = ''
            # dấu cách
            elif self.tok == ' ':
                self.tokens.append(['WHITESPACE'])
                self.tok = ''
        # trả về tokens
        return self.tokens
    def __checkBeginBuiltin(self):
        try:
            if self.tokens[-1][0][-4:] == 'SQRT' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                self.tokens[-1][-1] += self.tok
            else:
                self.tokens.append(['LPARENT', '('])
        except:
            self.tokens.append(['LPARENT', '('])
    def __checkEndBuiltin(self):
        try:
            if self.tokens[-1][0][-4:] == 'SQRT' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'SIN' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'COS' and not self.tokens[-1][-1].endswith(')') or self.tokens[-1][0] == 'TAN' and not self.tokens[-1][-1].endswith(')'):
                self.tokens[-1][-1] += self.tok
                if self.tokens[-1][0] == 'SIN' or self.tokens[-1][0] == 'COS' or self.tokens[-1][0] == 'TAN':
                    if self.angle == 'degree':
                        self.tokens[-1][-1] = f'{(eval(self.tokens[-1][-1])*math.pi)/180}'
            else:
                self.tokens.append(['RPARENT', ')'])
        except:
            self.tokens.append(['RPARENT', ')'])
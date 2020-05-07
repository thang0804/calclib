import math, sys
from . import CalclibException

class Lexer:
    angle = 'degree' # Đơn vị đo góc là 'degree' là default
    def __init__(self):
        # initialize
        self.__variable = {}
        self.__createVarData()
    def GetTokens(self, exp:str):
        if self.angle != 'degree' and self.angle != 'radian':
            raise CalclibException.AngleUnitError(f"no angle unit named '{self.angle}'")
        self.exp = exp
        self.tokens = []
        self.tok = ''
        # bắt đầu lấy self.tokens
        for char in self.exp:
            self.tok += char
            # thêm self.tokens nếu xuất hiện int
            if self.tok.isdigit():
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
            # dấu '!' cho factorial
            elif self.tok == '!':
                try:
                    if self.tokens[-1][0] == 'INT':
                        self.tokens[-1][0] = 'FACTORIAL'
                    else:
                        raise CalclibException.MathError("factorial value must be an integer")
                    self.tok = ''
                except CalclibException.MathError as exception:
                    raise exception
                except:
                    self.tokens.append(['FACTORIAL', '!'])
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
            elif self.tok == 'sqrt':
                try:
                    if self.tokens[-1][0] == 'INT':
                        self.tokens.append([f'{self.tokens[-1][-1]}SQRT', ''])
                        self.tokens.pop(-2)
                    else:
                        self.tokens.append(['SQRT', ''])
                except:
                    self.tokens.append(['SQRT', ''])
                self.tok = ''
            # dùng cho sin
            elif self.tok == 'sin':
                self.tokens.append(['SIN', ''])
                self.tok = ''
            # dùng cho cos
            elif self.tok == 'cos':
                self.tokens.append(['COS', ''])
                self.tok = ''
            elif self.tok == 'tan':
                self.tokens.append(['TAN', ''])
                self.tok = ''
            # biến
            elif self.tok in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if type(self.__variable[self.tok]).__name__ == 'int':
                    self.tokens.append(['INT', str(self.__variable[self.tok])])
                elif type(self.__variable[self.tok]).__name__ == 'float':
                    self.tokens.append(['FLOAT', str(self.__variable[self.tok])])
                self.__lexVarBuiltin()
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
    def __lexVarBuiltin(self):
        try:
            if self.tokens[-2][0][-4:] == 'SQRT'  and not self.tokens[-2][-1].endswith(')') or self.tokens[-2][0] == 'SIN' and not self.tokens[-2][-1].endswith(')') or self.tokens[-2][0] == 'COS' and not self.tokens[-2][-1].endswith(')') or self.tokens[-2][0] == 'TAN' and not self.tokens[-2][-1].endswith(')'):
                if self.tokens[-1][0] == 'INT' or self.tokens[-1][0] == 'FLOAT':
                    self.tokens[-2][-1] += self.tokens[-1][-1]
                    self.tokens.pop(-1)
        except:
            self.tok = ''
    def __createVarData(self):
        varName = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for var in varName:
            self.__variable[var] = None
    def sto(self, key:str, value:float):
        if key in self.__variable:
            self.__variable[key] = eval(str(value))
        else:
            raise NameError(f"variable '{key}' does not exists")

class Parser:
    def TryParse(self, tokens:list):
        # initialize
        self.tokens = tokens
        i = 0
        expr = '' # đây là biến xuất ra phép tính
        # lấy tokens để parse
        while i < len(self.tokens):
            if self.tokens[i][0] == 'INT' or self.tokens[i][0] == 'FLOAT':
                try:
                    # phát hiện số mũ và tính số mũ thành 1 số cho expr
                    if self.tokens[i+1][0] == 'POW':
                        expr += f'{eval(self.tokens[i][-1])**eval(self.tokens[i+1][-1])} '
                        i += 2
                    else:
                        expr += self.tokens[i][-1] + ' '
                        i += 1
                except:
                    expr += self.tokens[i][-1] + ' '
                    i += 1
            # thực hiện tính toán căn thức và đưa kết quả thêm vào "expr"
            elif self.tokens[i][0][-4:] == 'SQRT':
                if self.tokens[i][0][0:-4].isnumeric():
                    expr += f'{eval(self.tokens[i][-1])**(1/eval(self.tokens[i][0][0:-4]))} '
                else:
                    expr += f'{eval(self.tokens[i][-1])**(1/2)} '
                i += 1
            # thực hiện tính toán sin và đưa kết quả thêm vào "expr"
            elif self.tokens[i][0] == 'SIN':
                expr += f'{math.sin(eval(self.tokens[i][-1]))} '
                i += 1
            elif self.tokens[i][0] == 'COS':
                expr += f'{math.cos(eval(self.tokens[i][-1]))} '
                i += 1
            elif self.tokens[i][0] == 'TAN':
                expr += f'{math.tan(eval(self.tokens[i][-1]))} '
                i += 1
            elif self.tokens[i][0] == 'OP' or self.tokens[i][0] == 'LPARENT' or self.tokens[i][0] == 'RPARENT':
                expr += self.tokens[i][-1] + ' '
                i += 1
            # thực hiện tính factorial
            elif self.tokens[i][0] == 'FACTORIAL':
                expr += f'{self.__factorial(self.tokens[i][-1])} '
                i += 1
            elif self.tokens[i][0] == 'WHITESPACE':
                expr += ' '
                i += 1
        sys.tracebacklimit = 0
        expr = str(eval(expr))
        # nếu giá trị trả về là *.0 thì bỏ .0 và để parser trả về kiểu int thay vì *.0(float)
        if expr.endswith('.0'):
            expr = expr.replace('.0', '')
        # trả về kết quả đã làm tròn
        try:
            return round(eval(expr), 15)
        except Exception as e:
            raise e
    
    def __factorial(self, value):
        returned = 1
        for i in range(1, int(value)+1):
            returned *= i
        return returned
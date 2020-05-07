import math, sys

class Parser:
    def TryParse(self, tokens):
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
                        expr += f'{eval(self.tokens[i][-1])**eval(self.tokens[i+1][-1])}'
                        i += 2
                    else:
                        expr += self.tokens[i][-1]
                        i += 1
                except:
                    expr += self.tokens[i][-1]
                    i += 1
            # thực hiện tính toán căn thức và đưa kết quả thêm vào "expr"
            elif self.tokens[i][0][-4:] == 'SQRT':
                if self.tokens[i][0][0].isdigit():
                    expr += f'{eval(self.tokens[i][-1])**1/int(self.tokens[i][0][0])}'
                else:
                    expr += f'{eval(self.tokens[i][-1])**1/2}'
                i += 1
            # thực hiện tính toán sin và đưa kết quả thêm vào "expr"
            elif self.tokens[i][0] == 'SIN':
                expr += f'{math.sin(eval(self.tokens[i][-1]))}'
                i += 1
            elif self.tokens[i][0] == 'COS':
                expr += f'{math.cos(eval(self.tokens[i][-1]))}'
                i += 1
            elif self.tokens[i][0] == 'TAN':
                expr += f'{math.tan(eval(self.tokens[i][-1]))}'
                i += 1
            elif self.tokens[i][0] == 'OP' or self.tokens[i][0] == 'LPARENT' or self.tokens[i][0] == 'RPARENT':
                expr += self.tokens[i][-1]
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
            return round(eval(expr), 10)
        except Exception as e:
            raise e
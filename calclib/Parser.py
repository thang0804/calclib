class Parser:
    def TryParse(self, tokens):
        self.tokens = tokens
        i = 0
        expr = ''
        while i < len(self.tokens):
            if self.tokens[i][0] == 'INT' or self.tokens[i][0] == 'FLOAT':
                try:
                    if self.tokens[i+1][0] == 'POW':
                        expr += f'{eval(self.tokens[i][-1])**eval(self.tokens[i+1][-1])}'
                        i += 2
                    else:
                        expr += self.tokens[i][-1]
                        i += 1
                except:
                    expr += self.tokens[i][-1]
                    i += 1
            elif self.tokens[i][0] == 'OP' or self.tokens[i][0] == 'LPARENT' or self.tokens[i][0] == 'RPARENT':
                expr += self.tokens[i][-1]
                i += 1
        expr = str(eval(expr))
        if expr.endswith('.0'):
            expr = expr.replace('.0', '')
        return round(eval(expr), 10)
class AngleUnitError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return self.message

class MathError(Exception):
    def __init__(self, *args, errorcode=None):
        self.errorcode = errorcode
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.errorcode == 'FactorialError':
            self.message = "factorial value must be integer"
            return self.message
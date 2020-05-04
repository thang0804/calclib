class UnitError(Exception):
    def __init__(self, *args, unit=None):
        self.unit = unit
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f"{self.message}\"{self.unit}\""
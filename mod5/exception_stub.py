class BlockErrors:
    def __init__(self, errors):
        self.errors = errors

    def __enter__(self):
        return self.errors

    def __exit__(self, type, value, traceback):
        if type in self.errors or type.__base__ in self.errors:
            return True

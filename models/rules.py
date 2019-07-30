class Rules():
    """ Class that contains all the 256 rules.
    """
    def __init__(self):
        self.rules = {}
        self.init_rules()

    def init_rules(self):
        self.rules = {
            '1': [0, 0, 0, 0, 0, 0, 0, 0],
            '2': [0, 0, 0, 0, 0, 0, 0, 1],
            '3': [0, 0, 0, 0, 0, 0, 1, 0]
        }

    def get(self, n):
        return self.rules[n]

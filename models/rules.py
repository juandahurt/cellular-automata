from helpers.binary_converter import BinaryConverter


class Rules():
    """ Class that contains all the 256 rules.
    """
    def __init__(self):
        self.rules = {}
        self.init_rules()

    def init_rules(self):
        rule_n = 0 #  Rule number
        bin_converter = BinaryConverter()
        while (rule_n < 256):
            bin = bin_converter.convert_to_bin(rule_n)
            self.rules.update({ str(rule_n): bin })
            rule_n = rule_n + 1
            
    def get(self, n):
        return self.rules[n]

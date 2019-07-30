class BinaryConverter():
    """ This class has one and only one purpuse: convert a binary Number
        to a decimal number.
    """
    def convert(self, binary):
        dec = 0
        exp = 0
        for index in range(len(binary) - 1, -1, -1):
            dec = dec + binary[index] * pow(2, exp)
            exp = exp + 1
        return dec

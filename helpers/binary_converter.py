class BinaryConverter():
    """ This class has two purpuses: convert an 8-bit number
        to a decimal number (0 - 255) and vice versa.
    """
    def convert_to_dec(self, binary):
        dec = 0
        exp = 0
        for index in range(len(binary) - 1, -1, -1):
            dec = dec + binary[index] * pow(2, exp)
            exp = exp + 1
        return dec

    def convert_to_bin(self, dec):
        bin = [0] * 8
        index = 7
        while dec > 0:
            if dec % 2 == 0:
                bin[index] = 0
            else:
                bin[index] = 1
            dec = int(dec / 2)
            index = index - 1
        return bin

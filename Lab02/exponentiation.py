class Exponentiation:
    def __init__(self, number, exponent, module):
        self.NUMBER = number
        self.EXPONENT = exponent
        self.MODULE = module
        self.MODULE_LENGTH = module.bit_length()
        self.EXPONENT_LENGTH = exponent.bit_length()



    # Montgomery multiplication
    def MM(self, number1, number2):
        N = self.MODULE_LENGTH
        result = 0
        pos = 0
        while (pos < N):
            result += (number2 & 0x0001) * number1
            if (result & 0x0001): result += self.MODULE
            result >>= 1
            number2 >>= 1
            pos += 1
        if (result >= self.MODULE): result -= self.MODULE

        return result


    def evaluate(self):
        R = 1 << self.MODULE_LENGTH # multiplicative invertion
        print("R = {}".format(R))
        B = self.MM(self.NUMBER, (R * R) % self.MODULE)
        print("B = {}".format(B))
        result = R % self.MODULE
        print("Preresult = {}".format(result))
        print("==========================")
        pos = self.EXPONENT_LENGTH
        while (pos > 0):
            print("j = {}".format(pos-1))
            result = self.MM(result, result)
            print("Current result = {}".format(result))
            if ((1 << pos-1) & self.EXPONENT): 
                print("e(j) = {}".format(1 << pos-1))
                result = self.MM(result, B)
                print("Current result = {}".format(result))
            pos -= 1
            print("==========================")
        result = self.MM(result, 1)
        print("Final result = {}".format(result))

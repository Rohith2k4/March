//1009. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        flipped = ""

        for i in b:
            if i == '0':
                flipped += '1'
            else:
                flipped += '0'

        return int(flipped, 2)

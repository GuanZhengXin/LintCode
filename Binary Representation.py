"""
Given a (decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in
as a string. If the number can not be represented accurately in binary, return ERROR

Example
For n=3.72, return ERROR

For n=3.5, return 11.1
"""
from decimal import *

__author__ = 'Danyang'


class Solution:
    def binaryRepresentation(self, n):
        """
        difficult part: determine whether the fraction can be represented in binary

        if cannot represent, repeat forever, then cut-off at 32bit as int

        Notice: LintCode OJ has bug in test case 12 of this question
        :param n: Given a decimal number that is passed in as a string
        :return: A string
        """
        dec_part = ""
        if "." in n:
            int_part, dec_part = n.split(".")
            getcontext().prec = len(dec_part)+1
            dec_part = "."+dec_part
        else:
            int_part = n

        a = self.natural_num_to_bin(int(int_part))
        b = self.fraction_to_bin(Decimal(dec_part))

        if b=="ERROR":
            return "ERROR"

        if a=="":
            a = "0"
        if b=="":
            return a
        else:
            return a+"."+b

    @staticmethod
    def natural_num_to_bin(n):
        sb = []  # string buffer
        while n>0:
            sb.append(n&1)
            n >>= 1

        return "".join(map(str, reversed(sb)))

    @staticmethod
    def fraction_to_bin(n):
        sb = []
        while n>0:
            if len(sb)>32:
                return "ERROR"
            n *= Decimal(2)
            cur = int(n)
            sb.append(cur)
            n -= Decimal(cur)
        return "".join(map(str, sb))


if __name__=="__main__":
    print Solution().binaryRepresentation("0.6418459415435791")
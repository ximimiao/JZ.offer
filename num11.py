class Solution:
    """
    给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
    思路
    当指数为负数的时候，可以先对指数求绝对值，然后算出次方的结果之后再取倒数。
    如果底数为0，则直接返回0。此时的次方在数学上是没有意义的。

    """
    def Power(self, base, exponent):
        # write code here
        result = 1
        if base == 0:
            return False
        for i in range(abs(exponent)):
            result = result*base
        if exponent<0:
            result = 1/result
        return result
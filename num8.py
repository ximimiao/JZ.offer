class resolution:
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    思路
    当n=1时，结果为1；
    当n=2时，结果为2；
    当n=3时，结果为4；

以此类推，我们使用数学归纳法不难发现，跳法f(n)=2^(n-1)
    """
    def frog(self,n):
        if n <=2:
            return n
        result = 1
        for i in range(1,n):
            result *= 2
        return result
if __name__ == '__main__':
    s = resolution()
    n = input("共有多少层台阶")
    result = s.frog(int(n))
    print("共%d种方法"%result)

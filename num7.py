class resolution:
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
    斐波那契思想
    """
    def stage(self,n):
        if n==1:
            return 1
        if n==2:
            return 2
        first,second,third = 1,2,0
        for i in range(3,n+1):
            third = first+second
            first = second
            second = third
        return third
if __name__ == '__main__':
    s = resolution()
    n = input("共有多少层台阶")
    result = s.stage(int(n))
    print("共%d种方法"%result)

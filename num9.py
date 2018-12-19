class resolution:
    """
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
    请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法

    feibonaqie
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
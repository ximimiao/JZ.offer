class resolution:
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

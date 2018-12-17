class resolution:
    def Fibonacci(self,n):
        if n<=1:
            return n
        first,second,third = 0,1,0
        for i in range(2,n+1):
            third = first +second
            first = second
            second = third

        return third
if __name__ == '__main__':
    fibonacci = resolution()
    n = input()
    s = fibonacci.Fibonacci(int(n))
    print(s)
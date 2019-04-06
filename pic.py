import sys
# 读取第一行的n
n = str(sys.stdin.readline().strip())
num = int(sys.stdin.readline().strip())
s = ''
if num <0:
    print(-1)
else:
    for i in range(0,len(n)-num+1):
        a = n[i:i+num]
        s =s+a+' '
    print(s)
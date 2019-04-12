"""
小明、小华，是校内公认的数据算法大牛。两人组队先后参加了阿里云天池大赛多项奖金赛事，多次获奖，
小明是其中的队长。最近的一次工业数据智能竞赛中，两人又斩获季军，获得奖金1万元。

作为算法大牛，两人竞赛奖金分配也有独特方式，由两人共同编写的一个程序来决定奖金的归属。
每次获奖后，这个程序首先会随机产生若干0~1之间的实数{p_1, p_2, …, p_n}，然后从小明开始，
第一轮以p_1的概率将奖金全部分配给小明，第二轮以p_2的概率将奖金全部分配给小华，
这样交替地小明、小华以p_i的概率获得奖金的全部，一旦奖金被分配，则程序终止，
如果n轮之后奖金依旧没发出，则从p_1开始继续重复（这里需要注意，如果n是奇数
，则第二次从p_1开始的时候，这一轮是以p_1的概率分配给小华）；
直到100轮，如果奖金还未被分配，程序终止，两人约定通过支付宝将奖金捐出去。
单独一行，输出一个小数，表示小明最终获得奖金的概率
"""
import sys
n = int(sys.stdin.readline().strip(' '))
l = []
for i in range(n):
    n1 = sys.stdin.readline().strip(' ')
    l.append(float(n1))
result = 0
i=1
temp = 1.0000
while i<100:

    j = 0
    if i%2==1:
        while j<len(l):
            if j%2==0:
               temp=temp*l[j]
               result+=temp
            else:
               temp = temp*(1-l[j])
            j += 1
    else:
        while j<len(l):
            if j%2==0:
                temp=temp*(1-l[j])
            else:
                temp = temp*l[j]
                result+=temp
            j += 1
    i += 1
print('%.4f'%result)

import math
t = int(input())
while(t>0):
    a=(input())
    val=a.split(' ')
    b=int(val[1])
    print(int(math.log2(b)))
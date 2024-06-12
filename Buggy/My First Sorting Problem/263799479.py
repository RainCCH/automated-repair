t=int(input())

for i in range(t+1):
    x,y = map(int,input().split())
    if x<y:
        print(x," ",y)
    else:
        print(y," ",x)
        
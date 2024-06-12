d=input().split()
t=int(d[0])
x_c=[int(d[i]) for i in range(1,t+1)]
res=[]
for x in x_c:
    a=[]
    while x!=0:
        if x%2==0:
            a.append(0)
        else:
            a.append(1)
            x-=1
            if x%2==0:
                a.append(0)
            else:
                a.append(-1)
                x+=1
        x//=2
    res.append(a)
for a in res:
    n=len(a)
    print(n)
    print(" ".join(map(str,a)))
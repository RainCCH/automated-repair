t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    if(m==0):
        print(n)
        continue
    if(n>=m):
        l = n
        for k in range(1,m+1):
            l|=n-k
        r = n
        for k in range(1,m+1):
            r|=n+k
    else:
        l = arr[n]
        for k in range(1,n+1):
            l|=n-k
        r = n
        for k in range(1,m+1):
            r|=n+k
    print(l|r)
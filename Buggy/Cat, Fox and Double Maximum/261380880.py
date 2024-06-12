for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    q=[]
    for x in range(1,n//2+1):
        q.append(x)
        q.append(n+1-x)
    for x in range(q):
        print(x,end='')
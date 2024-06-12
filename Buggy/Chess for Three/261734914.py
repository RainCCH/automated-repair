a=int(input())
for i in range(a):
    b=list(map(int,input().split(' ')))
    ma=0
    s=b[0]+b[1]+b[2]
    if s%2==1:
        print("-1")
        continue
    if b[0]==b[1]==b[2]:
        print(str(s/2))
        continue
    while 0 in b:
        b.remove(0)
    while(len(b)>1):
        ma+=min(b)
        b[b.index(max(b))]-=min(b)
        b.remove(0)
        b.remove(min(b))
    print(str(ma))
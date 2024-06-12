t=int(input())
while t!=0:
    n=int(input())
    s=input()
    n=len(s)
    res=s.sort()
    if res == s:
        print("YES")
    else:
        print("NO")
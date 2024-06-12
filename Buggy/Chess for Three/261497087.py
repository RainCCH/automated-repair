for i in range(input()):
    a,b,c =map(int,input().split())
    if (a+b+c)%2!=0:
        print(-1)
    else:
        cur = sorted([a, b, c])
        ans = 0
        while cur[1] > 0:
            ans += 1
            cur[1] -= 1
            cur[2] -= 1
            cur = sorted(cur)
        print(ans)    
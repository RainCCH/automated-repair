t = int(input())
while(t):

    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    res = 0
    for i in range(n):
        res += abs(a[i]-b[i])

    flag = 1 


    for i in range(n):
        if(a[i]>=b[i]):
            if(b[i]<=b[-1]<=a[i]):
                flag = 0
                break
        else:
            if(a[i]<=b[-1]<=b[i]):
                flag = 0
                break
    mn = 0
    if(flag):
        mn = maxSize
        for i in range(n):
            mn = min(mn,abs(b[-1]-b[i]))
        for i in range(n):
            mn = min(mn,abs(b[-1]-a[i]))
         


    print(res+mn+1)

    t -= 1
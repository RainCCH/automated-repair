t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    a = 0
    if m == 0:
        print(n)
    else:
        for i in range(max(n-m,0),n+m+1,1):
            a = a|i 
        print(a)
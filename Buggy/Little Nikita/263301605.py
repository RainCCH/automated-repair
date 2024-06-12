n = int(input())

for i in range(n):
    a = int(input())
    b = list(map(int, input().split()))
    x = sorted(b)
    for j in range(a):
        b = b[1:] + b[:1]
        if b==x:
            print("yes")
            break
    else:
        print("no")
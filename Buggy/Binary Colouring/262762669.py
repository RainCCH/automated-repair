t = int(input())

for _ in range(t):
    x = int(input())

    ans = []

    for i in range(31):
        a = x & (1 << i)
        ans.append(1 if a > 0 else 0)

    i = 0
    while i < 31:
        j = i + 1
        if ans[i] == 1 and j < 32 and ans[j] == 1:
            while j < 32 and ans[j] == 1:
                j += 1
            ans[i] = -1
            for k in range(i + 1, j):
                ans[k] = 0
            ans[j] = 1
        i = j

    n = len(ans)
    while n > 0 and ans[n - 1] == 0:
        n -= 1

    print(n)
    for k in range(n):
        print(ans[k], end=" ")
    print()
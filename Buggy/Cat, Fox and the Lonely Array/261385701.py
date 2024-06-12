import sys

inp = sys.stdin.readline
out = sys.stdout.write

t = int(inp())

ar2 = [0] * (10**5)


def findMaxDist(n):
    # print(ar2[:n])
    i = -1
    d = 0
    md = 1
    while i < n:
        d += 1
        i += 1
        if ar2[i]:
            md = max(md, d)
            d = 0

    # print(md, d)
    return max(md, d)


for _ in range(t):
    n = int(inp())
    ar = list(map(int, inp().split()))
    maxDist = 1

    for i in range(0, 20):
        a = 2**i
        br = True
        ig = True
        for j in range(n):
            ar2[j] = ar[j] & a
            if ar2[j]:
                ig = False
            if ar[j] >= a:
                br = False
        if br:
            break
        if ig:
            continue
        maxDist = max(findMaxDist(n), maxDist)

    print(maxDist)
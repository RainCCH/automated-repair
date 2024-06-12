t = int(input())
def solve():
    n = int(input())
    m = int(input())
    x = (m+n) % 2
    if(x==0) and (m>n):
        print("YES")
    else:
        print("NO")

while (t>0):
    solve()
    t = t-1
n=int(input())
while(n>0):
    n=n-1
    size=int(input())
    inp=input()
    prev=ord(inp[0])
    op=1
    for i in range(0,size):
        if inp[i]>inp[i+1]:
            op=0
            break
    if op:
        print('YES')
    else:
        print('No')
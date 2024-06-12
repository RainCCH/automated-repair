t = int(input())
for i in range(t):
    score = 0
    n1 = int(input())
    n2 = int(input())  
    choice = n2
    for c in range(2,n2):
        if n2%c==0:
            print(n2//c)
            break
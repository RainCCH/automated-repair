e = int(input())
while e != 0: 
    n, m = input().split()
    if m > n:
        print("no")
    else:
        if m == n or (m % 2) == 0:
            print ("yes")
        else:
            print("no")
    e = e - 1
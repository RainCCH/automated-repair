t = int(input())
for _ in range(t):
    temp = str(input()).split(" ")
    n, m = temp[0], temp[1]

    if n % 2 == 0  and m % 2 == 0:
        print("No")
    else:
        print("Yes")
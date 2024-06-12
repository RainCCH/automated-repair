t = int(input()) 
output = []

for k in range(t):
    n = int(input())
    a = input()  #length of a = n
    b = input()  #length of a = n+1


    steps = 1
    diff = 0

    for i in range(n):
        diff = diff + min(diff, abs(int(a[i])-int(b[n])))
        diff = diff + min(diff, abs(int(b[i])-int(b[n])))

    for i in range(n):
        steps =  steps + abs(int(a[i])-int(b[i]))
        if(a[i]<=b[n]<=b[i] and b[i]<=b[n]<=a[i]):
            diff = diff +  0
    final = steps + diff 

    output.append(final)

print(output)
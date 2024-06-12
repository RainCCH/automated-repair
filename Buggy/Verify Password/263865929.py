def check(num,pwd):
    a=False
    count1=0
    b=False
    count2=0
    i=1
    while (i<num-1) and ord(pwd[i])<58 and ord(pwd[i])>46:
        if ord(pwd[i-1])-ord(pwd[i])<0:
            a=True
        i+=1
        
    while i<num-1:
        if ord(pwd[i])-ord(pwd[i+1])>30:
            return False                    #There is an digit after alphabet
        if (ord(pwd[i])-ord(pwd[i+1])<0):
            b=True    
        i+=1 
    if count1<=1:
        a=True
    if count2<=1:
        b=True
    return (a and b)

for _ in range(int(input)):
    n=int(input)
    s=input()
    if check(n,s):
        print("YES")
    else:
        print("NO")
            
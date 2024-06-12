for i in range(int(input())):
    l = list(bin(int(input()))[2:])
    for i in range(len(l)-1):
        if not l[i] =='0' and not l[i+1]=='0':
            if not i:
                l[i] = '0'
                if l[i+1]=='1':
                    l[i+1] = '0'
                else:
                    l[i+1] = '-1'
                flag = 1

                

            else:
                l[i-1],l[i] = ['1','0']
                if l[i+1]=='1':
                    l[i+1] = '0'
                else:
                    l[i+1] = '-1'
    if flag:
        l = ['1']+l
    print(len(l))
    print(*l[::-1])
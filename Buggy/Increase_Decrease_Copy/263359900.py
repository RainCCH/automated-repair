n=int(input())
for i in range(n):
    p=int(input())
    count=0
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    if(l1==l2):
        print(0)
    else:
        l1s=l1
        l2s=l2
        l1s.sort()
        l2s.sort()
        j=0
        k=0
        while( k < len(l2s)):
            if j >= len(l1s):                                   
                l1s.append(l1s[j-1])                            
                count+=1  
                count+=abs(l1s-l2s[j])
                k+=1
            if(l1s[j] != l2s[k]):
                if(len(l1s) != len(l2s)):
                    l1s.append(l1s[j])
                    count+=1
                count+=abs(l1s[j] - l2s[k])
                l1s[j] = l2s[k]
            j+=1
            k+=1
        for i in range(len(l1s)):          
            if(l1s[i] != l2[i]):          
                count+=1
        print(count)
        
import math
def bitwise_range_or(l,r):

    diff=r-l
    x=int(math.log(diff,2))
    ans=l
    for i in range(0,x+2):
        ans=ans|(1<<i)
    return ans
T=int(input())
 
for t in range(0,T):
    n,m=map(int,input().split(" "))
    left=n-m
    right=n+m
    
   
    if(left<0):
        left=0
    
    result = bitwise_range_orr(left, right)
    print(result)
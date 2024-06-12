for _ in range(int(input())):
     st=str(input())
     n=len(st)
     let,di,res=0,0,true
     if(st[0]>='a' and st[0]<='z'):
        let=1
     else:
        di=1
     for i in range(1,n):
         if(st[i]>='a' and st[i]<='z'):
            if let==1 and st[i-1]>st[i]:
              res=false
            let=1
            di=0
         else:
            if let==1 or (st[i-1]>st[i]):
               res=false
            let=0
            di=1
     if res:
        print("YES")
     else:
        print("NO")
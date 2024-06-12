for _ in range(int(input())):
      n,m= [int(i)for i in input().split()]
      seg = []
      for _ in range(m):seg += [[int(i)for i in input().split()]]
      v,order = [0]*(n+1),[0]*(n+1)
      q = int(input())
      for i in range(1,q+1):
            x = int(input())
            if v[x]:continue
            v[x] = 1
            order[x] = i
      be = 0
      res = n+8
      for i in range(1,n+1):be += v[i];v[i] = be
      for e in seg:
          l,r = e
          if v[r]  - v[l-1]>(r-l+1)//2:
                p = sorted([i  for i in order[l:r+1] if i > 0  ])
                res = min(res,p[(r-l+1)//2 ])
      print(res if res != n+8 else -1)
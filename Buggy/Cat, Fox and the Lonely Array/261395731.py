tc = int(input())
for _ in range(tc):
    prev_position = [-1]*20
    n = int(input())
    pos_diff = [-1]*20
 
    arr = []
    given = input().split()
    for _ in range(n):
        arr.append(int(given[_]))
    for i,num in enumerate(arr):
        for pos in range(20):
            if((num>>pos) & 1 ==1):
                pos_diff[pos] = max(pos_diff[pos],i-prev_position[pos])
                prev_position[pos] = i
    ans = 1
    for i in range(n):
      if(prev_position[i]!=-1):
        pos_diff[i]= max(pos_diff[i],n-prev_position[i])
        ans = max(ans,pos_diff[i])
    ans = ans if ans !=-1 else 1
    print(ans)
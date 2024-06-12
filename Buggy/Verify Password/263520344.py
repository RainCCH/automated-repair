def solve():
    n = int(input())
    s = input()
    num = []
    alp = []
    
    if s != s.lower():
        print('NO')
        
        return
    
    for i in range(n):
        if i < n and (s[i].isdigit() == False and s[i + 1].isdigit() == True):
            print('NO')
            
            return
        
        c = s[i]
        
        if c.isdigit():
            num.append(int(c))
        else:
            alp.append(c)
    
    if (num == sorted(num)) and (alp == sorted(alp)):
        print('YES')
    else:
        print('NO')
        
        
if __name__ == '__main__':
    for test in range(int(input())):
        solve()
        
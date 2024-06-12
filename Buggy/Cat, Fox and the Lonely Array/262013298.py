def loneliness(a):
    n = len(a)
    
    # Try all possible values of k
    for k in range(1, n+1):
        # Check if the condition is satisfied for all subarrays of length k
        satisfied = True
        target = a[0] | a[1] | ... | a[k-1]
        for i in range(n-k+1):
            if a[i] | a[i+1] | ... | a[i+k-1] != target:
                satisfied = False
                break
        
        if satisfied:
            return k
    
    # If no value of k satisfies the condition, return n
    return n

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(loneliness(a))
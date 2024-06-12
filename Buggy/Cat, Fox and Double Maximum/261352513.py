# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the length of the permutation and the permutation itself
    n = int(input())
    p = list(map(int, input().split()))

    # Initialize q as a sorted list of indices from 1 to n
    q = list(range(1, n + 1))

    # Sort q based on the difference pi + q[i] - pi-1 - q[i-1]
    q.sort(key=lambda i: p[i-1] + q[i-1])

    # Print the resulting permutation q
    print(*q)
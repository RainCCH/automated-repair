def get_an(n, m):
    # The initial sequence is 0, 1, 2, ...
    a = list(range(n + 1))

    # Simulate the changes for m seconds.
    for _ in range(m):
        # Update the elements of the sequence.
        for i in range(1, n + 1):
            a[i] = a[i - 1] | a[i] | a[i + 1]
        # Update the first element.
        a[0] = a[0] | a[1]

    # Return the value of a_n.
    return a[n]


# Get the number of test cases.
t = int(input())

# Process each test case.
for _ in range(t):
    # Get the values of n and m.
    n, m = map(int, input().split())

    # Calculate the value of a_n and print it.
    print(get_an(n, m))
def find_maximum(l, r):
    # Find the largest power of 2 within the range [l, r]
    max_power = 0
    while (1 << (max_power + 1)) <= r:
        max_power += 1

    if (1 << max_power) >= l:
        return max_power
    return max_power - 1

t = int(input())
results = []
for _ in range(t):
    l, r = map(int, input().split())
    results.append(find_maximum(l, r))

for resut in results:
    print(result)
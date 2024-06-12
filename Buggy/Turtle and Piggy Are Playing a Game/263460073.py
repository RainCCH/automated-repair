def max_score(l, r):
    return min(r // l, l)


def solve():
    data = input().split()

    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        l = int(data[index])
        r = int(data[index + 1])
        index += 2
        # Calculate the maximum score
        results.append(max_score(l, r))

    for result in results:
        print(result)


if __name__ == "__main__":
    solve()
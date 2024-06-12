def find_permutation(lst, m):
    list1 = lst[1:-1]
    min_el = min(list1)
    list1.remove(min_el)
    list_max = list1[::2]
    list_min = [lst[0]] + list1[1::2] + [lst[-1]]
    list_max.sort()
    list_min.sort(reverse = True)
    func = {}
    func[min_el] = m + 1
    j = 2 * m
    for el in list_max:
        func[el] = j
        j -= 1
    j = 1
    for el in list_min:
        func[el] = j
        j += 1
    res = []
    for key in lst:
        res.append(func[key])
    return res 

t = int(input())
for _ in range(t):
    m = int(input()) // 2
    start = [int(x) for x in input().split()]
    res = find_permutation(start, m)
    print(*res)
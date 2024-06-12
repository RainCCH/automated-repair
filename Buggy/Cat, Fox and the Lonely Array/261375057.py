def check_loneliness(arr, k):
    n = len(arr)
    seen = set()
    for i in range(n - k + 1):
        subarray_or = 0
        for j in range(k):
            subarray_or |= arr[i + j]
        if subarray_or in seen:
            return False
        seen.add(subarray_or)
    return True

def loneliness_of_array(arr):
    n = len(arr)
    low, high = 1, n
    while low < high:
        mid = (low + high) // 2
        if check_loneliness(arr, mid):
            high = mid
        else:
            low = mid + 1
    return low

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        print(loneliness_of_array(arr))

if _name_ == "_main_":
   main()
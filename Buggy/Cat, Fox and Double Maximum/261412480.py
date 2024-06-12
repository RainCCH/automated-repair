def sol(num_list,n):
    is_odd = 1
    for i in range(n):
        if (i != 0) and (i != n-1) and (num_list[i] == n):
            is_odd = i%2
    lst = []
    lst_ = []
    for i in range(n):
        if i%2 == is_odd:
            lst.append((num_list[i],i))
        else:
            lst_.append((num_list[i], i))
    lst = sorted(lst,key=lambda x: x[0])
    lst_ = sorted(lst_,key=lambda x: x[0])
    k = n
    for i in range(len(lst)):
        lst[i] = (lst[i][0]+k, lst[i][1])
        k -= 1
    for i in range(len(lst_)):
        lst_[i] = (lst_[i][0]+k, lst_[i][1])
        k-=1

    joined_lst = lst + lst_
    joined_lst = sorted(joined_lst, key=lambda x: x[1])

    for i in range(n):
        print(joined_lst[i][0]- num_list[i], end=' ')

def main():
    try:
        n_cases = int(input())
        for _ in range(n_cases):
            num = int(input())
            int_list = [int(x) for x in input().split()]
            sol(int_list)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
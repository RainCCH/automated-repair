def main():
    n = int(input())
    arr = [1, 2, 3]
    spectetor = 3
    winner = 0
    end = "YES"
    
    while n != 0:
        winner = int(input())
        if winner != spectetor:
            for i in range(3):
                if arr[i] != winner and arr[i] != spectetor:
                    spectetor = arr[i]
                    break
        else:
            end = "NO"
            break
        n -= 1
    
    print(end)

if __name__ == "__main__":
    main()
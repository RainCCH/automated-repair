n=int(input())
arrA=[]
arrB=[]
arrA_input = input().split(',')
for num in arrA_input:
    arrA.append(int(num))
arrB_input = input().split(',')
for num in arrB_input:
    arrB.append(int(num))

arrA.append(arrB[-1])
count=1
for i in range(n+1):
    if arrA[i]!=arrB[i]:
        value=arrA[i]-arrB[i]
        count=count+abs(value)
print(count)              
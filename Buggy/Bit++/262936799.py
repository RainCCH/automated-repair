e=0
for i in range(y):
    u=list(str(x) for x in input("").split())
    for j in u:
        if j == "++X" or j=="X++":
            e+=1
        elif j== "--X" or j=="X--":
            e-=1
print(e)
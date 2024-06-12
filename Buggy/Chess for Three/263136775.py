def chess_for_three(p1, p2, p3):
    ## write your solution here!
    # if p1==p2==p3:
    #     return -1
    # elif((p1+p2)<=p3):
    #     return (p1+p2)
    
    if (p1+p2+p3)%2:
        print (-1)
    elif((p1+p2)<=p3):
        print (p1+p2)
    
    else:
        print (int((p1+p2+p3)/2))
        
        
num=int(input())
for i in range (num):
    p1=int(input())
    p2=int(input())
    p3=int(input())
    chess_for_three(p1, p2, p3)
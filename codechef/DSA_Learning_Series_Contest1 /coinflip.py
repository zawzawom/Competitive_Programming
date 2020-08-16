T = int(input())
for i in range(T):
    G = int(input())
    for j in range(G):
        count = 1
        li = list(map(int,input().split()))
        if li[0]== li[2]:
            count = li[1]//2
        else :
           count = li[1]-li[1]//2
        print(count)
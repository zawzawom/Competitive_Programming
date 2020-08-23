for i in range(int(input())):
    N = int(input())
    li = list(map(int,input().split()))
    m = li[-1]
    array = [m]
    for a in range(N-2,-1,-1):
        if(li[a]>=m):
            m = li[a]
            array.append(m)
    for b in range(len(array)-1,-1,-1):
        print(array[b],end=" ")
    print()
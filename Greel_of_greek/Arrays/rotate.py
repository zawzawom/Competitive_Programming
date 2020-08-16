for i in range(int(input())):
    size,position=list(map(int,input().split()))
    li = range(size)
    li= list(map(int,input().split()))
    for a in range(size):
         print(li[(a+position)% size],end=" ")

######https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
for i in range(int(input())):
    size,position=tuple(map(int,input().strip().split()))
    li = range(size)
    li= list(map(int,input().strip().split()))
    for a in range(size):
         print(li[(a+position)% size],end=" ")
    print()
    #####new line for print() statement only#####
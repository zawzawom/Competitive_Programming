import numpy
for _ in range(int(input())):
    size = int(input())
    li = list(map(int,input().split()))
    for i in range(len(li)):
        for _ in range(i,len(li)):
           if all(a>=li[i] for a in li):
               print(li[i],end=' ')
               del li[i]
               break
    print()

try:
    t=int(input())
    for i in range(t):
        output = 0
        Ncars=int(input())
        N=list(map(int,input().split()))
        speed=N[0]
        for i in range(1,Ncars):
            if N[i]<speed:
                speed = N[i]
                output+=1
        print(output+1)
        
except:
    print("")
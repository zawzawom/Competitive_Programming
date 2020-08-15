T = int(input())
for i in range(T):
    Z = 0 
    N = int(input())
    while(0<N):
        Z = Z + N//5
        N = N//5
    # T = T - 1    
    print(Z)
    
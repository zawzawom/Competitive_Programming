try: 
    T = int(input())
    C = list()
    maximum = 0
    while(T):
        C.append(int(input()))
        T = T -1
    B= sorted(C)
    # print(B)
    # print("B1",B[1])
    for i in range(len(B)):
        B[i] = B[i] *(len(B)-i) 
        # print(B[i])
        if maximum <B[i] :
           maximum = B[i] 
    print(maximum)
except :
    pass
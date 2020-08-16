###############################################Reference############################
##https://www.geeksforgeeks.org/check-whether-large-number-given-form-multiple-3/###
####################################################################################
for i in range(int(input())):
    k,d0,d1 = list(map(int,input().split()))
    # print("k",k,d0,d1)
    temp = (d0 + d1)
    N=str(d0)+str(d1)
    # print(N)
    mul = 1
    for j in range(k+1-2):
        temp = int(temp)
        mul = mul * 2
        print(temp)
        temp =mul%10*(temp%10)
        N = N + str(temp)
    print("temp",temp,"N",N)

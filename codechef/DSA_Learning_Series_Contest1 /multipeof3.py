for a in range(int(input())):
    k,d0,d1 = list(map(int,input().split()))
    sum = 0
    sum = str(sum)
    temp = (d0 + d1)%10
    sum = str(d0) + str(d1)
    if (k<3):
        if int(sum)%3==0:
            print("YES")
        else:
            print("NO")
    sum = sum + str(temp)
    times = (k - 3)%d1
    for i in range(times):
        temp = (2 * temp)%10
        sum = sum + str(temp)
    if int(sum)%3==0:
        print("YES")
    else:
        print("NO")

    
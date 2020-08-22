#####Problem statement 
####https://www.codechef.com/LRNDSA01/problems/MULTHREE
for a in range(int(input())):
    k,d0,d1 = list(map(int,input().split()))
    sum = 0
    temp = d0 + d1
    if k ==2:
        s = temp
    else:
        sum = temp + (temp%10) + ((temp*2)%10 +(temp*4)%10 + (temp*8)%10 + (temp*6)%10 )*((k-3)//4)
        for i in range((k-3)-((k-3)//4)*4):
            sum+= (2 * temp)%10
            temp = 2 * temp
            
    if int(sum)%3==0:
        print("YES")
    else:
        print("NO")

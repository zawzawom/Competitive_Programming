xy = input()
x = xy[0]
y = xy[len(xy)-1]
print(xy)
count  = 0
count1 = 0
for i in range(len(xy)):
    if(xy[i]==x):
      count = count + 1
    elif(xy[i]==y):
      count1 = count1 + 1 
if(count*2==count1):
    print("Yes")
else:
    print("No")
print(count)
print(count1)
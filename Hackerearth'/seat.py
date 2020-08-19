# Write your code here
seat_type = ['WS','MS','AS']
for _ in range(int(input())):
    no = int(input())
    seat_no=no%12
    # print(seat_no)
    if(seat_no==1):
      print(no+11,seat_type[0])
    elif(seat_no==2):
        print(no+9,seat_type[1])
    elif(seat_no==3):
        print(no+7,seat_type[2])
    elif(seat_no==4):
        print(no+5,seat_type[2])
    elif(seat_no==5):
        print(no+3,seat_type[1])
    elif(seat_no==6):
        print(no+1,seat_type[0])
    elif(seat_no==7):
        print(no-1,seat_type[0])
    elif(seat_no==8):
        print(no-3,seat_type[1])
    elif (seat_no==9):
        print(no-5,seat_type[2])
    elif(seat_no==10):
        print(no-7,seat_type[2])
    elif(seat_no==11):
        print(no-9,seat_type[1])
    elif(seat_no==0):
        print(no-11,seat_type[0])

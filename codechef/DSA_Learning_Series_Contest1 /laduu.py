for i in range(int(input())):
    IND = input().split()
    count = 0 
    T2 = int(IND[0])
    for j in range(T2):
        win = input().split()
        # rank = int(win[1])
        position= win[0]
        if(position=="CONTEST_WON"):
             if(int(win[1])<20):
                count = count +300 +20 -int(win[1])
             else:
                 count = count + 300
        elif position =="TOP_CONTRIBUTOR":
            count = count + 300    
        elif position=="BUG_FOUND":
            count = count + int(win[1])
        elif position =="CONTEST_HOSTED" :
            count = count + 50
    if(IND[1]=="INDIAN"):
        print(count//200)
    else :
        print(count//400)

           
            
        
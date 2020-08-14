# ####gaga = ga ga
# abcde ab de
# rotor ro or
# xyzxy xy xy
# abbaab abb aab
# ababc ab bc
# ####
# ####

    ################

#######main function ###############

T = input()
try:
    T = input(T)
    while(T):
             T = T - 1
             text = input()
             num = int(len(text) % 2)
             if num == 0 :
               start = int(len(text)/2)
               str1 = sorted(text[0:start])
               str2 = sorted(text[start:])
               if str1 == str2: 
                  print("Yes")
               else :
                  print("NO")
             else:
               start = int(len(text)/2)
               str1 = sorted(text[0:start])
               str2 = sorted(text[start+1:])
               if str1 == str2: 
                   print("Yes")
               else :
                  print("NO")  
            
except:
        print("Enter Valid Input")


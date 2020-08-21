inp     = (input())
if(inp.islower):
   length   = len(inp)
   length2 = (length//2)
#    print(length2)
   if (length%2==0):
      
      test1 = sorted(inp[:length2])
      length = (length//2)
    #   print(length)
      test2 = sorted(inp[length:])
      if test1 ==test2:
          print("Yes")
      else:
          print("No")
        #   print(length)
   else:
      length = (length//2)+1
      test1 = sorted(inp[:length2])
      test2 = sorted(inp[length:])
      
      if test1 ==test2:
        print("Yes")
      else:
        print("No")
        # print(length)
        
      

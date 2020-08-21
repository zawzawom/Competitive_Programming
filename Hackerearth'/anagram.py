# # def anagram_fun(f_word, s_word):
# #     for i in range(len(f_word)):

# #         for j in range(len(s_word)):

# #              if f_word[i] == s_word[j]:
            
# #                     s_word = s_word[:j]+s_word[j+1:]
# #                     # print(s_word)
# #                     break
                    
# #     return len(s_word)
        
        
    
 

# # for i in range(int(input())):

# #     first_word = str(input())
    
# #     second_word = str(input())
    
# #     ##String Approach
    
# #     c1 = anagram_fun(first_word, second_word)
    
# #     c2 = anagram_fun(second_word, first_word)
    
# #     print(c1+c2)
# #########using STRING REPLACEMENT###########################
# def fun(test1,test2):
#     for i in range(len(test1)):
#         for j in range(len(test2)):
#             if(test1[i]==test2[j]):
#                 test2 = test2[:j]+test2[j+1:]
#                 break
#     return test2
# for _ in range(int(input())):
#     test1 = input()
#     test2 = input()
#     x = fun(test1,test2)
#     y = fun(test2,test1)
#     print(len(x)+len(y))
for _ in range(int(input())):
    test1 = list(input())
    test2 = list(input())
    count = 0
    length = len(test1)+len(test2)
    for i in range(len(test1)):
        for j in range(len(test2)):
          if(test1[i] == test2[j]):
            count=count + 2
            del test1[i]
            del test2[j]
            break
          else : 
            count = count + 0
        # print(count)
    length = length - count
    print(length)

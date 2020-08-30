# Competitive_Programming
[Big O notation](https://www.youtube.com/watch?v=__vX2sjlpXU)
* print('hello',end='') splict space
#Reverse Array in 10 ways
 * Using slicing array[::-1]
 * Using reverse() or reversed() method array.reverse(),new_list = list(reversed(array))
 <b> If you use reverse() it will the order of actual list.Hence,the orignal list items is lost.
     And the useage of reversed(),you need to create a new list and then put the list(reversed(array))
 * Using numpy
   `
    
    import numpy as np
    #The original NumPy array
    new_arr=np.array(['A','s','k','P','y','t','h','o','n'])
    print("Original Array is :",new_arr)
    #reversing using flip() Method or flipud()
    res_arr=np.flip(new_arr)
    print("Resultant Reversed Array:",res_arr)
  
   `

#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    listix = []
    listy = []
    for x, j in my_list:
        listix.append(x*j)
    for x, j in my_list:
        listy.append(j)
    return(sum(listix)/sum(listy))


           #second method :
       #liste comprehension : 
   #somme = sum([x*y for x, y in my_list])
  #return(somme/sum([y for x, y in my_list])

           #Third method :
       #Direct additions using Tuples :
   #     somme1, somme2 = 0
   #     for tulpe in my_list:
   #     somme1 +=(tulpe[0] * tulp[1])
   #     somme2 += tulp[1]
   #     somme1/somme2

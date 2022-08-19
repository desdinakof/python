def Nmaxelements(list_to_iterate, previous_list, iteration_number):
    if previous_list == None:
       previous_list = []
  
    for i in range(0, iteration_number): 
        max1 = 0
        for j in range(len(list_to_iterate)):     
            if list_to_iterate[j] > max1:
                max1 = list_to_iterate[j];
                  
        previous_list.append(max1)
        previous_list.append(list_to_iterate.index(max1))
 #       list_to_iterate.remove(max1);
    return previous_list

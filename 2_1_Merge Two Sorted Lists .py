
def mergeTwoLists(self, list1, list2):
    new_list= list1
    for i in range(len(list2)):
        new_list.append(list2[i])
     #sort new_list with selection sort
    for i in range(len(new_list)):
        min_index = i
        for j in range(i+1,len(new_list)):
            if new_list[min_index]>new_list[j]:
                min_index = j
        new_list[i],new_list[min_index] = new_list[min_index],new_list[i]

    return new_list


print(mergeTwoLists(1,[1,2,3,7],[0]))

    
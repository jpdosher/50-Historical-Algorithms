#find the max number in a List using recursion

def max_value(list):
 if len(list) == 2: #base case
    return list[0] if list[0] > list[1] else list[1] #compare elements
 sub_max = max_value(list[1:]) 
 return list[0] if list[0] > sub_max else sub_max

print(max_value([1,20,3,10]))

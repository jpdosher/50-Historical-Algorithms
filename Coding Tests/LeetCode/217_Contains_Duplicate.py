nums = [1,2,4,1]

def containsDuplicate(nums) -> bool:    
    unique_values = list(set(nums))
    print(unique_values)
    return True if len(unique_values) != len(nums) else False
    
    
print(containsDuplicate(nums))
#quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot] #
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5,2,3,1,4,6]))
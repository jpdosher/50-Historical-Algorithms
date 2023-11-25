import cProfile

#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        # Traverse the array, skipping the already sorted elements
        for j in range(i + 1, len(arr)):
            # If the current element is smaller than the minimum element
            if arr[min_index] > arr[j]:
                min_index = j  # Update the index of the minimum element
        # Swap the elements
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([4,2,3,1]))
cProfile.run('selection_sort([])')


def selection_Sort(arr):
    for i in range (len(arr)):
        indice_valor_min = i
        for j in range (i+1, len(arr)):
            if arr[j] < arr[indice_valor_min]:
                indice_valor_min = j
        arr[i], arr[indice_valor_min] = arr[indice_valor_min], arr[i]
    return arr

print(selection_Sort([4,2,3,1]))
cProfile.run('selection_Sort([])')


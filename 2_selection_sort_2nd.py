def findSmallest(arr):
    smallest = arr[0] 
    smallest_index = 0 
    for i in range(1, len(arr)): # Percorre o array a partir do segundo elemento até o último elemento
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for j in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))     # Remove o menor elemento do array e adiciona ao novo array
    return newArr
    
print(selectionSort([4,2,30,1]))
#soma array com recursao
def soma_array(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + soma_array(array[1:])
    
print(soma_array([2,4,6]))
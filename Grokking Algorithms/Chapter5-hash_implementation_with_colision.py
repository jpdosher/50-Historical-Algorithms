#hash function implementation in python with colision
def hash(key):
    return key % 10
def insert(hash_table,key,value):
    hash_key = hash(key)
    hash_table[hash_key] = value

def search(hash_table,key):
    hash_key = hash(key)
    return hash_table[hash_key]

def delete(hash_table,key):
    hash_key = hash(key)
    hash_table[hash_key] = None
    return hash_table[hash_key]


hash_table = [None] * 10 #tamaho da tabela

insert(hash_table,1,10)
insert(hash_table,2,20)
insert(hash_table,3,320)
insert(hash_table,4,40)
insert(hash_table,5,50)

print(search(hash_table,3))

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.

def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_region = [s,t]
    apples = list(map(lambda x:x+a,apples))
    oranges = list(map(lambda x:x+b, oranges))
    apples_in = len([x for x in apples if x in range(house_region[0], house_region[1]+1)])
    oranges_in = len([x for x in oranges if x in range(house_region[0], house_region[1]+1)])

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
import cProfile

#fibonacci with recursive function
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#test cases
print(fib(1)) #1
print(fib(10)) #1
print(fib(22)) #2
print(fib(30)) #3
print(fib(100)) #5

print(cProfile.run('fib([100])'))

# #example of another recursive function
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))

# def hello():
#     print("hello function")
#     hello()

# import sys
# max_recursion = sys.getrecursionlimit()
# print(max_recursion)
# def countdown(start):
#     """ countdown from a number"""
#     print(start)
#     if start < 20:
#         countdown(start+1)
# countdown(1)

def fact(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f
result = fact(5) 
print(result)

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    print(factorial(5))



















    







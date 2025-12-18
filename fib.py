# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(100))

memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result

print(fib(44))
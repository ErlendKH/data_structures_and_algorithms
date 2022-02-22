
def factorial(n):
    if n == 1:
        return 1
    # 
    return n * factorial(n-1)

# factorial(4)
# return 4 * factorial(3) = 4 * 6 = 24
# return 3 * factorial(2) = 3 * 2 = 6
# return 2 * factorial(1) = 2 * 1 = 2
# return 1

print(factorial(4)) # 24

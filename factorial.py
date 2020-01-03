def factorial(n):
    sum = 1
    for i in range(2, n+1):
        sum  = sum * i
    return sum


def factorial_2(n):
    if n < 3:
        return n
    result = 2
    for i in range(3, n+1):
        result *= i
        return result

def rc_factorial(n):
    if n < 3:
        return n
    return n * rc_factorial(n-1)

print(rc_factorial(5))
print(factorial_2(3))

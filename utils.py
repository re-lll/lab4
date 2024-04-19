def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
<<<<<<< Updated upstream
=======

def degree(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    while n % 5 == 0:
        n /= 5
    return n == 1

def degree2(n):
    return n & (n - 1) == 0 and n != 0
>>>>>>> Stashed changes

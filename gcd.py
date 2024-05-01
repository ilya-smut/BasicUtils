# Euclidian Algorithm for finding GCD

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
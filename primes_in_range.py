from math import sqrt


def primes_from_range(a, b):
    for x in range(a, b + 1):
        for d in range(2, x):
            if x % d == 0:
                print(f'{x} divides by {d}, so it is NOT a prime number.')
                break
        else:
            print(f'{x} is a prime number.')


def primes_from_range_optimized(a, b):
    for x in range(a, b + 1):
        for d in range(2, int(sqrt(float(x)))+1):
            if x % d == 0:
                print(f'{x} divides by {d}, so it is NOT a prime number.')
                break
        else:
            print(f'{x} is a prime number.')


primes_from_range(2, 15)
primes_from_range_optimized(2, 15)
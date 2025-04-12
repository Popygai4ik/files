import fnmatch
import math


def is_semiprime(x):
    primes = []
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0 and is_prime(i):
            j = x // i
            if i != j and is_prime(j):
                return True
    return False

def is_prime(x):
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
for x in range(0, 10**8, 1579):
    if fnmatch.fnmatch(str(x), '132?5*5??') and is_semiprime(x):
        print(x,x/1597)

import fnmatch
import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_semiprime(x):
    primes = []
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0 and is_prime(i):
            j = x // i
            if i != j and is_prime(j):
                return True
    return False

for x in range(0, 10**8, 1597):  # делится на 1597
    if fnmatch.fnmatch(str(x), '132?5*5??'):
        if is_semiprime(x):
            print(x, int(x / 1597))

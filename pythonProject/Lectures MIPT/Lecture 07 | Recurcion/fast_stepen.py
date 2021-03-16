import math
import decimal
from decimal import *

def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n-1) * a
    else:
        return pow(a**2, n//2)


z = (pow(99, 99))




getcontext().prec = 28

print(z)


print(math.frexp(z))
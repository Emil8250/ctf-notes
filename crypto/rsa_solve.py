from Crypto.Util.number import long_to_bytes
import gmpy2
import math


#Solve simple RSA with known values
def decrypt(p, q, e, ct):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    pt = pow(ct, d, n)
    return long_to_bytes(pt).decode()

#Decrypt RSA where primes are equal
def decrypt2(n, e, ct):
    p = int( gmpy2.iroot(n,2)[0])
    phi = pow(p, 2) - p
    d = pow(e, -1, phi)
    pt = pow(ct, d, n)
    return long_to_bytes(pt).decode()
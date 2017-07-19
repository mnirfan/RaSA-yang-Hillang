"modifikasi dari https://github.com/mgermino/RSA"

import list_magic as lm
import numpy as np
import h

def hill(n, key):
    (ciphered, key_decrypt) = h.crypt(message=n, n=2, cipher_matrix=key)
    return (ciphered, key_decrypt)


def encrypt(e, n, m):
    """
    Given e, n, and m return a number

    >>> encrypt(17, 377, 102)
    163
    >>> encrypt(25, 237, 42)
    183
    >>> encrypt(47, 367, 82)
    30
    """

    return m ** e % n



def encryptlist(e, n, lon):
    """
    Given e, n (the modulus, and a list of numbers, encrypt each number
    in the list and return a list of encrypted values.

    >>> encryptlist(17, 377, [277, 52, 40, 121])
    [36, 364, 235, 270]
    >>> encryptlist(25, 237, [137, 62, 30, 151])
    [173, 65, 114, 184]
    >>> encryptlist(47, 367, [58, 322, 465, 230])
    [285, 329, 289, 245]
    """


    return [encrypt(e, n, m) for m in lon]


def encryptstr(e, n, s):
    """
    given e, and n, select a number (c) return the decrypted value.

    >>> encryptstr(17, 377, "discrete")
    [341, 287, 202, 99, 95, 69, 116, 69]
    >>> encryptstr(23, 422, "rabbit")
    [224, 409, 124, 124, 383, 162]
    >>> encryptstr(33, 672, "legend")
    [384, 293, 391, 293, 608, 64]
    """
    list_data = encryptlist(e, n, [ord(c) for c in list(s)])
    print("list terenkripsi:", list_data)
    return lm.list2int(list_data)

def decrypt(d, n, c):
    """
    Given d and n are given, select a number (c) and return the decrypted value.

    >>> decrypt(257, 377, 341)
    100
    >>> decrypt(186, 255, 461)
    106
    >>> decrypt(256, 300, 657)
    201
    """
    return c ** d % n


def decryptlist(d, n, dalist):

    """

    >>> decryptlist(257, 377, [341, 287, 202, 99, 96, 69, 116, 69])
    [100, 105, 115, 99, 5, 101, 116, 101]
    >>> decryptlist(257, 377, [56, 287, 556, 235, 22, 45, 354, 78])
    [374, 105, 225, 40, 42, 197, 178, 169]
    >>> decryptlist(257, 377, [256, 35, 456, 543, 32, 56, 667, 245])
    [94, 120, 118, 147, 301, 374, 348, 267]
    """

    return [x ** d % n for x in dalist]

def decryptint(d, n, int_number):
    encrypted_list = lm.int2list(int_number)
    # print("list:", encrypted_list)
    decrypted_list =  decryptlist(d, n, encrypted_list)
    string = ""
    for ascii_code in decrypted_list:
        string += chr(ascii_code)

    return string

def gcd(a, b):
    """
    given a and b, return the greatest common divisor

    >>> gcd(75, 21)
    3
    >>> gcd(52, 81)
    1
    >>> gcd(27, 18)
    9
    >>> gcd(300, 42)
    6
    >>> gcd(254, 60)
    2
    """
    while b !=0:
        (a, b) = (b, a%b)
    return a

def phi(p, q):
    return (p - 1) * (q - 1)

def liste(p, q):
    """
    generates a list of available encryption exponents from p and q

    >>> liste(5, 11)
    [3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99]
    >>> liste(17, 25)
    [5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73, 77, 79, 83, 85, 89, 91, 95, 97]
    >>> liste(25, 92)
    [5, 11, 17, 19, 23, 25, 29, 31, 37, 41, 43, 47, 53, 55, 59, 61, 67, 71, 73, 79, 83, 85, 89, 95, 97]
    """
    phii = phi(p, q)
    alpha = []
    for i in range(2, 100):
	    if gcd(i, phii) == 1:
		    alpha.append(i)
    return alpha

def finde(p, q):
    """
    takes p and q and selects a random number from a generated list
    """
    date = liste(p, q)
    from random import choice
    return choice(date)


def egcd(a,b):
    """
    Given a, and b, calculates the egcd and returns the x and y values
    >>> egcd(9, 6)
    (1, -1)
    >>> egcd(51, 0)
    (1, 0)
    >>> egcd(1,0)
    (1, 0)
    """
    if b == 0:
        return (1, 0)
    else:
        q = a // b
        r = a % b
        (s, t) = egcd (b, r)
        return (t, s-q*t)

def findd(e, p, q):
    """
    finds the value of d with the values of p and q

    >>> findd(91, 5, 11)
    11
    >>> findd(65, 17, 25)
    65
    >>> findd(23, 13, 20)
    119
    """
    phiin = phi(p, q)
    for d in range(1, 10000):
        if e * d % phiin == 1:
            return d



def genkeys(p, q):
    """
    generates random keys from p and q
    """
    phin = phi(p, q)
    alpha = []
    for i in range(2, 100):
	    if gcd(i, phin) == 1:
		    alpha.append(i)
    elist = alpha
    date = liste(p, q)
    from random import choice
    e = choice(date)
    for d in range(1, 10000):
	    if e * d % phin == 1:
		    return (e, d, phin, p*q)





if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)

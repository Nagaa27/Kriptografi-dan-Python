################################################################
# Kriptomath                                                                                             #
# Editor : Matius Celcius Sinaga                                                                 #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                      #
################################################################

def gcd(a, b):
    #menghasilkan GCD pada a dan b menggunakkan Algoritma Euclid
    while a != 0:
        a, b = b % a, a
    return b

def menentukanAturanKebalikan (a, m):
    #menghasilkan invers modular a % m,
    #dimana jumlah x sama seperti
    # a*x % m = 1

    if gcd(a, m) != 1:
        return None
    #tanpa pembagian mod inverse if a & m bukan bilangan prima

    #hitung menggunakan algoritma Euclidean
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # adalah operator pembagian integer
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

#jalankan shell lalu ikuti hal berikut
#import kriptomath
#kriptomath.gcd(1995, 27)


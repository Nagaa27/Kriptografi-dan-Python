################################################################
# Angka Primer Sieve                                                                                       #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

import math

def adalahPrimer(angka):
    #menghasilkan True apabila angka adalah angka primer
    #contohnya adalah bahwa angka dibawah 2 adalah bukan primer
    #menghasilkan True apabila angka yang dimaksud angka primer, vice versa 
    if angka < 2:
        return False

    #jika sebuah angka dapat dibagi dua dengan setiap angka hingga
    #perpangkatan dua akar dari angka tersebut
    for i in range(2, int(math.sqrt(nomor)) + 1):
        if angka % i == 0:
            return False
    return True


def SievePrimer(ukuranSieve):
    #menghasilkan sebuah daftar angka primer yang dapat dihitung
    #menggunakan algoritma Sieve dari Eratosthenes
    sieve = [True] * ukuranSieve
    #angka nol dan satu (dibawah dua) bukanlah angka primer
    sieve[0] = False
    sieve[1] = False

    #proses menghasilkan sieve
    for i in range(2, int(math.sqrt(ukuranSieve)) + 1):
        pointer = i * 2
        while pointer < ukuranSieve:
            sieve[pointer] = False
            pointer += i
    #mengkompilasi daftar angka primer
    primes = []
    for i in range(ukuranSieve):
        if sieve[i] == True:
            primes.append(i)

    return primes

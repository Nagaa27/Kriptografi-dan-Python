################################################################
# Rabin Miller                                                                                                 #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

import random

def rabinMiller(angka):
    #mengembalikan nilai Benar jika num adalah angka primer

    s = angka - 1
    t = 0
    while s % 2 == 0:
        #s tetap setengah hingga menghasilkan nilai genap
        #gunakan t untuk menghitung berapa banyak jumlah setengah dari s
        s = s // 2
        t += 1

    for mencoba in range(5):
    #mencoba untuk memalsukan 5 kali angka primer
        a = random.randrange(2, angka - 1)
        v = pow(a, s, angka)
        if v != 1:
        #test ini tidak akan menerima jika v adalah 1
            i = 0
            while v != (angka - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % angka
    return True

def adalahPrimer(angka):
    #menghasilkan True jika num adalah angka primer
    #fungsi ini lberjalan lebih cepat
    #angka primer melakukan cek sebelum memanggil rabinMiller()
    if (angka < 2) :
        return False

    #0, 1, dan angka negatif bukanlah angka primer
    #1/3 kali lebih cepat anda mampu menentukan jika num bukanlah angka primer
    #dengan membagi dengan yang pertama beberapa lusin angka primer
    #hal ini lebih cepat dari rabinMiller(), namun berbeda dengan rabinMiller hal ini tidak menjamin
    #menunjukkan bahwa angka tersebut adalah primer
    primerDasar = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if angka in primerDasar:
        return True

    #melihat apakah setiap angka kecil primer dapat dibagi dengan angka
    for prime in primerDasar:
        if (angka % prime == 0):
            return False

    #jika seluruh kemungkinan gagal, panggil rabinMiller() untuk menentukan jika num adalah angka primer
    return rabinMiller(angka)

def generateLargePrime (ukuranKunci=1024):
    #menghasilkan angka primer yang acak dari ukuran kunci
    while True:
        angka = random.randrange(2**(ukuranKunci-1), 2**(ukuranKunci))
        if isPrime(angka):
            return angka

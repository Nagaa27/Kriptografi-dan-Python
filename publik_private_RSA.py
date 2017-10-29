################################################################
# Membuat kunci RSA publik/private                                                                  #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

import random, sys, os, rabinMiller, kriptomath


def main():
    #membuat kunci publik dan privat dengan 1024 bit kunci
    print('Sedang membuat kunci...')
    buatKunciFile('matius_celcius_sinaga', 1024)
    print('Kunci file sudah dibuat.')

def hasilkanKunci(ukuranKunci):
    #membuat sebuah kunci publik dan private dengan kunci dengan ketentuan panjang kunci
    #hal ini akan berlangsung sedikit lebih lama dibandingkan program lainnya

    #langkah pertama, buatlah dua angka primer p dan q. Hitung n = p * q
    print('Mengubah p primer...')
    p = rabinMiller.menghasilkanAngkaPrimeryangLuas(ukuranKunci)
    print('Mengubah q primer...')
    q = rabinMiller.menghasilkanAngkaPrimeryangLuas(ukuranKunci)
    n = p * q

    #langkah kedua, buatlah angka a dimana e menjadi lebih relatif menjadi primer (p-1)*(q-1)
    print('Mengubah e menajdi angka primer yang lebih relatif menjadi (p-1)*(q-1)...')
    while True:
        #tetap mencoba dengan angka acak hingga e mencapai nilai yang benar
        e = random.randrange(2 ** (ukuranKunci - 1), 2 ** (ukuranKunci))
        if kriptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    #langkah ketiga, menghitung d, kebalikan mod dari e
    print('Menghitung d menjadi kebalikan mod dari e...')
    d = kriptomath.menentukanAturanKebalikan(e, (p - 1) * (q - 1))
    kunciPublik = (n, e)
    kunciPrivat = (n, d)

    print('Kunci Public :', kunciPublik)
    print('Kunci Private :', kunciPrivat)

    return (kunciPublik, kunciPrivat)

def buatKunciFile(nama, ukuranKunci):
    #membuat dua file 'x_pubkey.txt' dan 'x_privkey.txt' dimana x menjadi nilai nama
    #dengan n, e and d, e bilangan bulat yang ditulis dengan batasan koma

    #mengecek untuk mencegah penulisan kunci yang terlalu banyak dari kunci file 
    if os.path.exists('%s_pubkey.txt' % (nama)) or os.path.exists('%s_privkey.txt' % (nama)):
        sys.exit('PERHATIAN : bahwa file %s_pubkey.txt atau %s_privkey.txt sudah ada! Gunakan nama berbeda atau hapus dan ulangi kembali program ini' % (nama, nama))

    kunciPublik, kunciPrivat = hasilkanKunci(ukuranKunci)

    print()
    print('Kunci publik adalah %s dan a %s banyak angka.' % (len(str(kunciPublik[0])), len(str(kunciPublik[1]))))
    print('Menulis kunci publik pada file %s_pubkey.txt...' % (nama))
    fo = open('%s_pubkey.txt' % (nama), 'w')
    fo.write('%s,%s,%s' % (ukuranKunci, kunciPublik[0], kunciPublik[1]))
    fo.close()

    print()
    print('Kunci private adalah %s dan a %s banyak angka.' % (len(str(kunciPublik[0])), len(str(kunciPublik[1]))))
    print('Menulis kunci publik pada file %s_privkey.txt...' % (nama))
    fo = open('%s_privkey.txt' % (nama), 'w')
    fo.write('%s,%s,%s' % (ukuranKunci, kunciPrivat[0], kunciPrivat[1]))
    fo.close()

#jika keseluruhan program sudah berjalan dengan benar juga program yang diimport sudah berjalan dengan semestinya
if __name__ == '__main__':
    main()

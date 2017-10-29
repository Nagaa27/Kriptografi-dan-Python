################################################################
# Sandi Affine                                                                                                 #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

#modul sys diimport untuk keperluan fungsi exit()
#sudah tersedia pada saat menginstal Python
#modul pyperclip diimport untuk keperluan fungsi copy()
#modul kriptomath diimport untuk keperluan fungsi gcd() dan cariModMembalikkan
import sys, pyperclip, kriptomath, random
#memasukkan seluruh simbol yang mungkin akan digunakan nantinya
#termasuk diantaranya huruf besar dan kecil
#juga angka dan simbol, termasuk spasi berada di depan urutan
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" 

#fungsi pada main() hampir sama dengan main() pada program transposisi
def main():
    pesanSaya = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    kunciSaya = 2023
    #pada modeSaya silahkan ubah apakah enkripsi maupun dekripsi
    modeSaya = 'enkripsi' 

    #disini diatur agar memberikan nilai enkripsi pesanSaya
    if modeSaya == 'enkripsi':
        ubah = enkripsiPesan(kunciSaya, pesanSaya)
    #disini diatur apabila akan menghasilkan nilai dekripsi pesanSaya
    elif modeSaya == 'dekripsi':
        ubah = dekripsiPesan(kunciSaya, pesanSaya)
    print('Kunci: %s' % (kunciSaya))
    print('%si :' % (modeSaya.title()))
    print(ubah)
    #penggunaan pyperclip
    pyperclip.copy(ubah)
    print('Seluruh %s teks telah disalin.' % (modeSaya))

#kunci akan diubah menjadi kunciA dan kunciB
#contoh perhitungannya akan menjadi seperti
#kunciA 2023 // 95 atau 21
#kunciB 2023 % 95 atau 28
def cariBagianKunci(kunci):
    kunciA = kunci // len(SYMBOLS)
    kunciB = kunci % len(SYMBOLS)
    #hal ini akan memberikan hasil lebih cepat untuk kemudian digunakan berulang
    return (kunciA, kunciB)

#enkripsi dengan affine chiper melibatkan karakter dalam SYMBOLS menjadi berkalilipat
#dimana perkalian kunciA dan kunciB, kunciA = 1 dan kunciB = 0
#string akan melewati sys.exit(), fungsi ini akan menjadi pilihan fungsi parameter opsional
#yang akan ditampilkan pada layar sebelum program dijalankan
#hal ini juga berarti digunakan pada pesan error sebelum program berakhir
def cekKunci(kunciA, kunciB, mode):
    if kunciA == 1 and mode == 'enkripsi':
        sys.exit('Sandi Affine akan menjadi lebih lemah ketika A di tentukan menjadi 1. Silahkan pilih kunci yang berbeda.')
    if kunciB == 0 and mode == 'enkripsi':
        sys.exit('Sandi Affine akan menjadi lebih lemah ketika B di tentukan menjadi 0. Silahkan pilih kunci yang berbeda.')
    if kunciA < 0 or kunciB < 0 or kunciB > len(SYMBOLS) - 1:
        sys.exit('Kunci A harus lebih besar daripada 0 dan kunci B harus ada diantara 0 dan %s.' % (len(SYMBOLS) - 1))
    if kriptomath.gcd(kunciA, len(SYMBOLS)) != 1:
        sys.exit('Kunci A (%s) dan simbol ukuran yang ditentukan (%s) secara realtif bukanlah yang paling utama. Silahkan pilih kunci yang berbeda.' % (kunciA, len(SYMBOLS)))


def enkripsiPesan(kunci, pesan):
    kunciA, kunciB = cariBagianKunci(kunci)
    cekKunci(kunciA, kunciB, 'enkripsi')
    sanditeks = ''
    for symbol in pesan:
        if symbol in SYMBOLS:
            #untuk melakukan enkripsi anda harus menghitung jumlah kata yang akan dienkripsi
            #dengan melakukan perkalian pada symIndex dengan kunciA dan kunciB
            #lalu membagi nilai dengan ukuran simbol
            #jumlah yang anda hitung akan menjadi nilai SYMBOL karakter yang terenkripsi
            symIndex = SYMBOLS.find(symbol)
            sanditeks += SYMBOLS[(symIndex * kunciA + kunciB) % len(SYMBOLS)]
        else:
            #tambahkan apabila terdapat simbol yang tidak terenkripsi
            sanditeks += symbol 
    return sanditeks


def dekripsiPesan(kunci, pesan):
    kunciA, kunciB = cariBagianKunci(kunci)
    cekKunci(kunciA, kunciB, 'dekripsi')
    teksawal = ''
    kunciUntukMembalikkanA = kriptomath.cariModMembalikkan(kunciA, len(SYMBOLS))

    for symbol in pesan:
        if symbol in SYMBOLS:
            #melakukan dekripsi pada SYMBOL dengan menggunakan kunci untuk membalikkan
            symIndex = SYMBOLS.find(symbol)
            teksawal += SYMBOLS[(symIndex - kunciB) * kunciUntukMembalikkanA % len(SYMBOLS)]
        else:
            #tambahkan apabila terdapat simbol yang tidak terdekripsi
            teksawal += symbol 
    return teksawal


def menentukanKunciAcak():
    #disini akan dilakukan perulangan
    #jika perulangan  tidak pernah salah akan menjadi perulangan yang tiada akhir
    #jika program melakukan perulangan terus menerus, karena perulangan tidak menghasilkan nilai False
    #untuk berhenti maka tekan Ctrl-C atau Ctrl-D
    while True:
        kunciA = random.randint(2, len(SYMBOLS))
        kunciB = random.randint(2, len(SYMBOLS))
        if kriptomath.gcd(kunciA, len(SYMBOLS)) == 1:
            return kunciA * len(SYMBOLS) + kunciB


#apabila semua sudah berjalan termasuk modul yang diimport di dalamnya
#fungsi main akan mulai berjalan dari sini disini
if __name__ == '__main__':
    main()

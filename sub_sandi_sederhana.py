################################################################
# Sub Sandi Sederhana                                                                                     #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                       #
################################################################

import pyperclip, sys, random

HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    pesanSaya = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    kunciSaya = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    #program ini akan melakukan enkripsi
    modeSaya = 'enkripsi' 

    cekKebenaranKunci(kunciSaya)

    if modeSaya == 'enkripsi':
        ubah = pesanEnkripsi(kunciSaya, pesanSaya)
    elif modeSaya == 'dekripsi':
        ubah = pesanDekripsi(kunciSaya, pesanSaya)
    print('Menggunakan kunci %s' % (kunciSaya))
    print('Kunci %sed pesan:' % (modeSaya))
    print(ubah)
    pyperclip.copy(ubah)
    print()
    print('Pesan sedang disalin kedalam layar.')

#fungsi cekKebenaranKunci melakukan validasi/pemeriksaan kunci
#apakah kunci sudah digunakan, lalu mengurutkannya
#apabila sudah digunakan akan memberikan pesan kesalahan
def cekKebenaranKunci(kunci):
    daftarKunci = list(kunci)
    daftarHuruf = list(HURUF)
    #pada sort() seluruh hasil modifikasi ditempatkan dan tidak memberi nilai pengembalian
           #untuk mengatur daftarKunci dan daftarHuruf secara bersamaan
           #karena daftarKunci adalah karakter yang berasal dari HURUF
       #jika daftarkunci dan daftarHuruf adalah sama, anda dapat mengetahui bahwa daftarKunci
            #tidak memiliki salinan di dalamnya, karena HURUF tidak memiliki salinan di dalamnya
    daftarKunci.sort()
    daftarHuruf.sort()
    
#setiap nilai dari karakter di dalam simbol dicek
#tanpa melakukan duplikasi tanpa adanya kehilangan huruf yang digunakan
#pada daftarKunci nilai variabel pada daftar kunci dikembalikan
#di mulai dari huruf A - Z, simbol dan angka yang digunakan
    if daftarKunci != daftarHuruf:
        sys.exit('Ditemukan sebuah error pada kunci atau simbol.')

#salah satu cara untuk memasukkan fungsi dan memanggilnya dua kali tanpa harus membuat lagi
#pertama, hal ini tidak perlu di kode program lagi
#kedua, jika ada bug/kesalahan/celah dalam kode yang diduplikasi
#anda hanya perlu memperbaiki bug tersebut sekali pada dua tempat berbeda
#hal ini lebih baik daripada mengganti kode yang sudah diduplikat dengan satu fungsi yang memiliki kode
def pesanEnkripsi(kunci, pesan):
    return ubahPesan(kunci, pesan, 'enkripsi')

def pesanDekripsi(kunci, pesan):
    return ubahPesan(kunci, pesan, 'dekripsi')

#fungsi ubahPesan melakukan enkripsi/dekripsi tergantung mode yang ditetapkan
#proses enkripsinya sangat mudah, pada setiap kata dalam parameter pesan
#lalu menggantinya dengan parameter kunci dan begitu sebaliknya(untuk dekripsi)
def ubahPesan(kunci, pesan, mode):
    ubah = ''
    karakterA = HURUF
    karakterB = kunci
    if mode == 'dekripsi':
        
        #untuk dekripsi, anda dapat menggunakan kode enkripsi yang sama
        #anda hanya perlu melakukan persamaan dimana kunci dan HURUF digunakan
        karakterA, karakterB = karakterB, karakterA

    #lompati seluruh SYMBOL dalam pesan
    for symbol in pesan:
        if symbol.upper() in karakterA:

            #proses encrypt/decrypt the symbol
            #string isupper() akan mengembalikan nilai benar apabila :
            #string memiliki setidaknya satu huruf kapital
            #string tidak memiliki satu huruf kecil
            #string islower() akan mengembalikan nilai benar apabila :
            #string memiliki setidaknya satu huruf kecil
            #string tidak memiliki satu huruf kapital
            symIndex = karakterA.find(symbol.upper())
            if symbol.isupper():
                ubah += karakterB[symIndex].upper()
            else:
                ubah += karakterB[symIndex].lower()
        else:
            #symbol bukan bagian dari HURUF, hanya tambahan saja
            ubah += symbol
    return ubah


def menentukanKunciAcak():
    kunci = list(HURUF)
    random.shuffle(kunci)
    return ''.join(kunci)


if __name__ == '__main__':
    main()

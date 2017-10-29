################################################################
# Test/ujicoba Transposisi                                                                                 #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

#random dan sys sudah tersedia pada python saat anda melakukan instalasi
#enkripsitransposisi dan dekripsitransposisi adalah program sebelumnya
#tempatkan enkripsitransposisi dan dekripsitransposisi berada pada folder yang sama
import random, sys, enkripsitransposisi, dekripsitransposisi

def main():
    #mengatur settingan acak "seed" menjadi nilai statis
    #mengubah algoritma dan menentukan nilai 42
    #hal ini disebut juga sebagai PSEUDORANDOM NUMBERS
    #pada random.randint juga menghasilkan PSEUDORANDOM NUMBERS
    #secara teknis nilai yang dihasilkan random.randint() sesungguhnya tidaklah acak
    #dan hasil algoritmanya dapat anda prediksi 
    random.seed(42)

    #batasi jumlah test hanya mencapai 20 test saja
    for i in range(20): 

      #contohnya jika anda menentukan seed antara 1 hingga 10 akan menentukan nilai acak 7
        pesan = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        #ubah pesan string menjadi daftar yang akan di acak
        pesan = list(pesan)
        random.shuffle(pesan)
        pesan = ''.join(pesan) 
       #list/daftar diubah menjadi string

        print('Test #%s: "%s..."' % (i+1, pesan[:50]))

        #cek seluruh kemungkinan kunci untuk setiap pesan
        for kunci in range(1, len(pesan)):
            dienkripsi = enkripsitransposisi.enkripsiPesan(kunci, pesan)
            didekripsi = dekripsitransposisi.dekripsiPesan(kunci, dienkripsi)

            #jika dekripsi tidak cocok dengan pesan asli
            #akan menampilkan error dan keluar
            if pesan != didekripsi:
                print('Tidak cocok dengan kunci %s dan pesan %s.' % (kunci, pesan))
                print(didekripsi)
                sys.exit()

    print('Uji coba sandi Transposisi berhasil.')
                
        #jika testransposisi.py berjalan (dengan mengimport sebuah modul
        #panggil main() fungsi
if __name__ == '__main__':
    main()

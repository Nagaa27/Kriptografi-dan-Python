###############################################################
# Sandi Caesar                                                                                                #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

#modul adalah program python yang memiliki fungsi tambahan
#yang  dimana dapat digunakan pada program lainnya
#modul pyperclip berada pada halaman lampiran buku ini
import pyperclip

pesan = 'Indonesia Raya'

#jumlah nilai langkah/sandi geser yang akan anda gunakan pada kunci
#silahkan ganti dengan angka yang anda inginkan
#kunci 9 berarti huruf yang pertama diubah menjadi huruf ke 9 
#dalam urutan abjad
kunci = 9

#apabila akan melakukan enkripsi maka isi dengan enkripsi
#begitu juga dengan sebaliknya apabila ingin melakukan dekripsi
mode = 'encrypt'

#setiap huruf pada HURUF akan digunakan pada program
#pastikan tidak ada yang terlewatkan
HURUF ='ABCDEFGHIJKLMNOPWRSTUVWXYZ'

ubah = ''

#mengubah setiap huruf menjadi huruf kapital
pesan = pesan.upper()

# seluruh huruf akan diproses dan ditentukan nilai enkripsi/dekripsinya 
for symbol in pesan:
    if symbol in HURUF:
        #enkripsi dan dekripsi pesan dilakukan disini
        #dengan menentukan jumlah symbol/huruf terlebih dahulu
        nomor = HURUF.find(symbol)
        if mode == 'encrypt':
            nomor = nomor + kunci
        elif mode == 'decrypt':
            nomor = nomor - kunci

        #jika pesan yang diproses lebih besar dari atau lebih kecil
        #atau sama dengan nol/tidak ada
        if nomor >= len(HURUF):
            nomor = nomor - len(HURUF)
        elif nomor < 0:
            nomor = nomor + len(HURUF)

        #jumlah symbol pada proses enkripsi/dekripsi ditambahkan
        #pada proses akhir pengubahan
        ubah = ubah + HURUF[nomor]
    else:
        #menambahkan simbol tanpa melakukan proses enkripsi/dekripsi
        ubah = ubah + symbol

#menampilkan hasil enkripsi/dekripsi pada tampilan
print(ubah)

#menyalin hasil enkripsi/dekripsi pada penyimpanan sementara 
pyperclip.copy(ubah)

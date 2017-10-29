################################################################
# Meretas sandi Caesar dengan Brute-force                                                          #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                       #
################################################################

pesan = 'JOEPOFTJB SBZB'
#kumpulan HURUF yang digunakan untuk menebak huruf kunci
HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#coba seluruh kunci yang memungkinkan
for kunci in range(len(HURUF)):

    #ubah tetap memiliki string kosong seperti sebelumnya telah dijelaskan
    ubah = ''

#bagian akhir dari proram ini hampir sama dengan program asli Caesar Cipher
#kode enkripsi dan dekripsi berjalan dan melakukan tugasnya pada string pesan
    for symbol in pesan:
        if symbol in HURUF:
            #mencari jumlah simbol dalam huruf
            nomor = HURUF.find(symbol)
            nomor = nomor - kunci

            #menangani proses dimana jumlah lebih dari 26 atau kurang dari 0
            if nomor < 0:
                nomor = nomor + len(HURUF)
            #tambahkan jumlah simbol pada akhir pengubahan
            ubah = ubah + HURUF[nomor]
        else:
            #tambahkan symbol tanpa melakukan enkripsi/dekripsi
            ubah = ubah + symbol

  #tampilkan kunci yang telah dicoba selama melakukan dekripsi
    print('Key #%s: %s' % (kunci, ubah))


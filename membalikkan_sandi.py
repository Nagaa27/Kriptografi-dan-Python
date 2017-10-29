################################################################
# Membalikkan Sandi                                                                                       #
# Editor  : Matius Celcius Sinaga                                                                        #
# Author : http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

#pesan berisi kata/kalimat yang nantinya akan disusun secara terbalik
#contoh pesan yang akan diubah adalah "Hello World!" maka hasilnya "!dlroW olleH"
#nantinya akan menjadi Hello World
pesan = 'Indonesia Raya'

#mengenalkan ubah dan nantinya akan menyimpan string yang telah diubah
#ingat bahwa string yang digunakan adalah dua single qoute (' ')
#bukan double karakter
ubah = ''

#panjang pesan akan dikurangi 1 dari posisi awal untuk menentukan barisan
i = len(pesan) - 1

#pada while akan ditentukan apakah True maupun False
#jika nilai i yang dihasilkan True maka program dilanjukan pada blok selanjutnya
#jika nilai False maka akan langsung melompat ke print
while i >= 0:
    
    #melakukan penyimpanan nilai dan pengubahan string ke bentuk lain
    #dalam bentuk lain yang dimaksud disebut dengan enkripsi
    ubah = ubah + pesan[i]
    i = i - 1

#hasil yang telah diubah akan ditampilkan dan program dijalankan
print(ubah)

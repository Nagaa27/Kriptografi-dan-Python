################################################################
# Enkripsi Transposisi                                                                                      #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

import pyperclip

#fungsi (fungsi main) memiliki statemen def
#def tidak disebut sebagai fungsi bernama main()
#def berarti membuat, atau defining, sebuah fungsi bernama main()
#yang kemudian dapat anda panggil/digunakan kembali pada program
def main():
    pesanSaya = 'Indonesia Raya Tanah Airku:IRTA'
    kunciSaya = 8

    sanditeks = enkripsiPesan(kunciSaya, pesanSaya)

    #menampilkan hasil enkripsi dalam bentuk ciphertext pada layar
    #dengan a | (dikenal sebagai "pipe" karakter) setelah hal tersebut akan ada ruang
    #pada akhir pesan yang telah dienkripsi
    print(sanditeks + '|')

    #salin string yang telah dienkripsi dalam chipertext pada tampilan layar
    pyperclip.copy(sanditeks)

def enkripsiPesan(kunci, pesan):
   #setiap string dalam ciphertext menghasilkan sebual kolom
    sanditeks = [''] * kunci

    #perulangan dilakukan pada setiap kolom dalam ciphertext
    for col in range(kunci):
        pointer = col

        #tetap melakukan perulangan hingga pointer berada pada nilai pesan terakhir
        while pointer < len(pesan):
            #menempatkan karakter pada titik pesan yang terakhir
            #pada kolom di dalam daftar ciphertext
            sanditeks[col] += pesan[pointer]

            #pindah pada akhit pointer
            pointer += kunci

    #ubah daftar ciphertext hingga nilai string tunggal dan mengulang
    return ''.join(sanditeks)


#jika enkripsitransposisi.py sedang berjalan (didalam modul yang telah diimport)
#panggil fungsi main()
if __name__ == '__main__':
    main()

################################################################
# Dekripsi dengan sandi Transposisi                                                                   #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

#program math sudah tersedia disaat anda melakukan instalasi python
import math, pyperclip

def main():
    #ubah disini apabila ingin mengganti pesan dan kunci
    #pesanSaya
    #kunciSaya
    pesanSaya = 'Iaakn nudRa:oahIny ReaATs iAiTr|'
    kunciSaya = 8

    teksawal = dekripsiPesan(kunciSaya, pesanSaya)

    #tampilkan dengan pipe ("|") setelah hal tersebut terbentuk
    #berikan spasi pada akhir pesan yang telah di dekripsi
    print(teksawal + '|')
    pyperclip.copy(teksawal)

def dekripsiPesan(kunci, pesan):
    #fungsi dekripsi transposisi akan menyimulasikan "kolom dan "baris"
    #pada tiap-tiap teks awal yang dituliskan berdasarkan daftar pada string
    #pertama, anda harus menghitung beberapa nilai
    #jumlah "kolom' dalam transposisi 
    #math.ceil adalah operator pembagian dimana akan menghasilkan nilai bulat
    #contohnya jika nilai yang dihasilkan 4,2 maka akan dibulatkan menjadi 4
    #jika nilai yang dihasilkan 4,9 maka akan dibulatkan menjadi 5 
    jumlahKolom = math.ceil(len(pesan) / kunci)

    #jumlahBaris adalah kunci
    jumlahBaris = kunci

    #jumlah kotak yang terisi adalah jumlah kolom baris dan pesan 
    jumlahKotakyangTerisi = (jumlahKolom * jumlahBaris) - len(pesan)

    #setiap string yang berada pada teks awal menghasilkan kolom
    teksawal = [''] * jumlahKolom

    #setelah karakter dienkripsi maka pesan selanjutnya
    kolom = 0
    baris = 0

    for symbol in pesan:
        teksawal[kolom] += symbol
        kolom += 1 
       #setelah itu akan dilanjutkan pada kolom selanjutnya

        #jika ada kolom lebih atau adanya baris yang tidak sesuai, maka
        #kembali pada kolom pertama dan melanjutkannya
        if (kolom == jumlahKolom) or (kolom == jumlahKolom - 1 and baris >= jumlahBaris - jumlahKotakyangTerisi):
            kolom = 0
            baris += 1

    return''.join(teksawal)

#jika transposisidekripsi.py sudah berjalan (setelah module di import)
#panggil fungsi if  main()
if __name__=='__main__':
    main()

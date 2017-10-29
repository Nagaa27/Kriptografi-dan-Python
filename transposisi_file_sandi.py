################################################################
# Transposisi File sandi                                                                                    #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

import time, os, sys, enkripsitransposisi, dekripsitransposisi

def main():
    #siapkan sebuah file teks berisi kata maupun kalimat
    #dengan nama file matiuscelciussinaga.txt (txt format teks)
    masukkanNamaFile = 'matiuscelciussinaga.txt'
    #jika nama file sudah ada dengan file yang akan anda gunakan
    #maka program akan melakukan perubahan pada nama file matiuscelciussinaga.txt
    namaFileKeluaran = 'matiuscelciussinaga.encrypted.txt'
    kunciSaya = 10
    #tentukan disini apakah dilakukan enkripsi atau dekripsi
    modeSaya = 'encrypt' 
    

   #jika file yang dimaksudkan belum ada, maka program terlebih dahulu melakukan eliminasi
    if not os.path.exists(masukkanNamaFile):
        print('File %s yang dimaksud tidak ada. Silahkan keluar...' % (masukkanNamaFile))
        sys.exit()

    #jika file yang dimaksud sudah ada, menghasilkan pilihan
    #untuk melanjutkan atau untuk berhenti
    if os.path.exists(namaFileKeluaran):
        print('Tulis ulang file %s. (C)ontinue atau (Q)uit?' % (namaFileKeluaran))
        response = input('> ')
        #startswith akan mengenalkan bahwa nilai masukkan yang dimulai dengan huruf C
        if not response.lower().startswith('c'):
            #secara teknis user tidak memberi nilai masukkan C maupun Q
            #karena program akan keluar disaat sys.exit() dipanggil
            sys.exit()

    #membaca pesan dari file yang telah dimasukkan
    objekFile = open(masukkanNamaFile)
    isi = objekFile.read()
    objekFile.close()

    #fungsi dari title() akan mengubah huruf pertama
    #setiap kalimat menjadi huruf kapital
    print('%sing...' % (modeSaya.title()))

    #mengukur panjang enkripsi/dekripsi yang dilakukan
    #time.time() akan menghitung berapa lama waktu program berjalan
    #dan menyimpan variabel waktuAwal
    waktuAwal = time.time()
    if modeSaya == 'encrypt':
        ubah = enkripsitransposisi.enkripsiPesan(kunciSaya, isi)
    elif modeSaya == 'decrypt':
        ubah = dekripsitransposisi.dekripsiPesan(kunciSaya, isi)
    jumlahWaktu = round(time.time() - waktuAwal, 2)
    print('%sion time: %s seconds' % (modeSaya.title(), jumlahWaktu))

    #menghasilkan pesan yang diubah menjadi file yang baru untuk ditampilkan
    FileObjekKeluaran = open(namaFileKeluaran, 'w')
    FileObjekKeluaran.write(ubah)
    FileObjekKeluaran.close()

    print('Done %sing %s (%s characters).' % (modeSaya, masukkanNamaFile, len(isi)))
    print('%sed file is %s.' % (modeSaya.title(), namaFileKeluaran))


#jika transposisifilechiper.py telah berjalan (termasuk seluruh modul didalamnya)
#panggil fungsi main()
if __name__ == '__main__':
    main()

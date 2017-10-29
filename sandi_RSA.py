################################################################
# Sandi RSA                                                                                                   #
# Editor : Matius Celcius Sinaga                                                                        #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

import sys

#ukuran blok harus lebih kecil daripada atau sama dengan ukuran kunci
#ukuran blok dalam bytes, ukuran kunci dalam bits
#ada 8 bits dalam 1 byte
UKURAN_BLOK_STANDAR = 128
#maksudnya terdapat 128 bytes
UKURAN_BYTE = 256
#dalam satu byte memiliki 256 nilai yang berbeda

def main():
    #jalankan sebuah test yang mengenkripsi sebuah pesan dalam sebuah file atau mendekrip sebuah pesan dari file
    namafile = 'encrypted_file.txt'
    #file untuk menulis atau untuk membaca
    mode = 'encrypt'
    #tentukan apakah enkripsi atau dekripsi

    if mode == 'encrypt':
        pesan = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
        namaKunciFilePublik = 'matius_celcius_sinaga_pubkey.txt'
        print('Mengenkripsi dan menulis dalam %s...' % (namafile))
        teksTerenkripsi = enkripsidantulisDalamFile(namafile, namaKunciFilePublik, pesan)

        print('Teks yang telah dienkripsi :')
        print(teksTerenkripsi)

    elif mode == 'decrypt':
        namaKunciFilePrivate = 'matius_celcius_sinaga_privkey.txt'
        print('Membaca dari %s dan mendekripsikan...' % (namafile))
        pesanTerdekripsi = membacadariFiledanDekripsi(namafile, namaKunciFilePrivate)

        print('Teks yang telah dekripsi:')
        print(pesanTerdekripsi)

def menetapkanBlokblokDariTeks (pesan, ukuranBlok=UKURAN_BLOK_STANDAR):
    #mengubah sebuah pesan menjadi sebuah daftar blok bilangan bulat
    #setiap bilangan bulat menghasilkan 128 (ukuran ukuranBlok) karakter

    pesanDalamByte = pesan.encode('ascii')
    #mengubah bilangan bulat menjadi bytes

    blockInts = []
    for mulaiBlok in range(0, len(pesanDalamByte), ukuranBlok):
        #menghitung blok bilangan bulat pada blok pada teks
        blockInt = 0
        for i in range(mulaiBlok, min(mulaiBlok + ukuranBlok, len(pesanDalamByte))):
            blockInt += pesanDalamByte[i] * (UKURAN_BYTE ** (i % ukuranBlok))
        blockInts.append(blockInt)
    return blockInts

def menetapkanTeksDariBlokblok (blockInts, panjangPesan, ukuranBlok=UKURAN_BLOK_STANDAR):
    #mengubah daftar blok bilangan bulat pada pesan asli
    #pesan asli panjang yang dibutuhkan secara khusus
    #untuk mengubah bilangan bulat blok terakhir
    pesan = []
    for blockInt in blockInts:
        pesanBlok = []
        for i in range (ukuranBlok - 1, -1, -1):
            if len(pesan) + i < panjangPesan:
                #mengubah pesan string menjadi 128
                #sesuai dengan ukuranBlok
                #karakter pada blok bilangan bulat
                angkaASCII = blockInt // (UKURAN_BYTE ** i)
                blockInt = blockInt % (UKURAN_BYTE ** i)
                pesanBlok.insert(0, chr(angkaASCII))
        pesan.extend(pesanBlok)
    return ''.join(pesan)

def enkripsiPesan(pesan, kunci, ukuranBlok=UKURAN_BLOK_STANDAR):
    #mengubah pesan menjadi daftar blok bilangan bulat
    #lalu enkripsi setiap blok bilangan bulat
    #melalui kunci PUBLIK untuk enkripsi
    blokTerenkripsi = []
    n, e = kunci

    for blok in menetapkanBlokblokDariTeks(pesan, ukuranBlok):
        # ciphertext = plaintext ^ e mod n
        blokTerenkripsi.append(pow(blok, e, n))
    return blokTerenkripsi

def dekripsiPesan(blokTerenkripsi, panjangPesan, kunci, ukuranBlok=UKURAN_BLOK_STANDAR):
    #dekrip daftar blok enkripsi yang ada menjadi pesan asli
    #panjang pesan asli yang dibutuhkan harus sesuai dengan blok akhirnya
    #pastikan agar kunci privatnya untuk melakukan dekripsi
    blokTerdekripsi = []
    n, d = kunci
    for blok in blokTerenkripsi:
        #teks awal = sandi teks ^ d mod n
        blokTerdekripsi.append(pow(blok, d, n))
    return menetapkanTeksDariBlokblok(blokTerdekripsi, panjangPesan, ukuranBlok)

def membacaKunciFile(namaFileKunci):
    #berikan nama file untuk setiap file yang memiliki kunci publik atau private
    #menghasilkan kunci sebagai berikut (n,e) atau (n,d) nilai tuple
    fo = open(namaFileKunci)
    content = fo.read()
    fo.close()
    ukurankunci, n, EorD = content.split(',')
    return (int(ukurankunci), int(n), int(EorD))

def enkripsidantulisDalamFile(namaFilePesan, namaFileKunci, pesan, ukuranBlok=UKURAN_BLOK_STANDAR):
    #dengan menggunakan kunci dari file kunci, enkripsi seluruh pesan dan simpan menjadi file
    #menghasilkan pesan yang sudah dienkripsi
    ukurankunci, n, e = membacaKunciFile(namaFileKunci)

    #cek bahwa ukuran kunci lebih besar daripada ukuran blok
    if ukurankunci < ukuranBlok * 8:
    #* 8 ubah bytes menjadi bits
        sys.exit('ERROR: Ukuran blok adalah %s bits dan ukuran kunci adalah %s bits. RSA cipher membutuhkan ukuran blok yang sama atau lebih besar daripada ukuran kunci. Begitu juga dengan kenaikan ukuran blok atau menggunakan kunci yang berbeda.' % (ukuranBlok * 8, ukurankunci))

    #mengenkripsi pesan
    blokTerenkripsi = enkripsiPesan(pesan, (n, e), ukuranBlok)

    #menguah nilai lebih besar dari satu jenis nilai lainnya
    for i in range(len(blokTerenkripsi)):
        blokTerenkripsi[i] = str (blokTerenkripsi[i])
    kontenYangTerenkripsi = ','.join(blokTerenkripsi)

    #menuliskan pesan yang sudah terenkripsi pada hasil keluaran file
    kontenYangTerenkripsi = '%s,%s,%s' % (len(pesan), ukuranBlok, kontenYangTerenkripsi)
    fo = open(namaFilePesan, 'w')
    fo.write(kontenYangTerenkripsi)
    fo.close()
    #juga menghasilkan string yang terenkripsi
    return kontenYangTerenkripsi

def membacadariFiledanDekripsi(namaFilePesan, namaFileKunci):
    #dengan menggunakan kunci pada file kunci, membaca sebuah pesan terenkripsi dari sebuah file lalu mendekripnya
    #menghasilkan pesan terdekripsi dalam bentuk string
    ukurankunci, n, d = membacaKunciFile(namaFileKunci)

    #membaca panjang pesan dan mengenkripsi pesan tersebut dari file
    fo = open(namaFilePesan)
    content = fo.read()
    panjangPesan, ukuranBlok, pesanTerenkripsi = content.split('_')
    panjangPesan = int(panjangPesan)
    ukuranBlok = int(ukuranBlok)

    #cek bahwa ukuran kunci lebih besar dari ukuran blok
    if ukurankunci < ukuranBlok * 8:
    # * 8 diubah dari bytes menjadi bits
        sys.exit('ERROR : Ukuran blok adalah %s bits dan ukuran kunci adalah %s bits. RSA cipher membutuhkan ukuran blok yang sama atau lebih besar daripada ukuran kunci. Apakah anda telah benar-benar memeriksa kunci file dan melakukan enkripsi pada file ?' % (ukuranBlok * 8, ukurankunci))

    #mengubah pesan terenkripsi hingga menjadi lebih besar dari nilai integer
    blokTerenkripsi = []
    for blok in pesanTerenkripsi.split(','):
        blokTerenkripsi.append(int(blok))

    #mendekrip nilai int yang lebih besar
    return dekripsiPesan(blokTerenkripsi, panjangPesan, (n,d), ukuranBlok)

#jika rsaCipher.py sudah berjalan termasuk didalamnya seluruh modul maka panggil fungsi main()
if __name__ == '__main__':
    main()

################################################################
# Meretas Sub Sandi Sederhana                                                                         #
# Editor : Matius Celcius Sinaga                                                                      #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                      #
################################################################

#langkah-langkah eksekusi program
#1.Temukan pola/aturan kata pada setiap pesan kata dalam pesan teks
#2.Temukan daftar kandidat bahasa pada pesan kata yang akan di dekrip
#3.Buatlah pemetaan huruf pada setiap pesan kata dengan menggunakan daftar kandidat pesan kata
#4.Eliminasi setiap pemetaan huruf
#5.Pindahkan setiap huruf yang telah dieliminasi pada pemetaan
import os, re, copy, pprint, pyperclip, subsandisederhana, membuatpolakata

if not os.path.exists('polaKata.py'):
    membuatpolakata.main() 
import polaKata

HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
bukanHurufatauPolaSpasi = re.compile('[^A-Z\s]')

def main():
    pesan = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    #mencoba melakukan validasi pada ciphertext
    print('sedang meretas...')
    pemetaanHuruf = retasSubSederhana(pesan)

    #munculkan hasil yang sudah didapatkan
    print('Melakukan pemetaan:')
    pprint.pprint(pemetaanHuruf)
    print()
    print('Pesan sandi yang Asli:')
    print(pesan)
    print()
    print('Menyalin pesan yang sudah diretas ke dalam layar:')
    pesanYangTeretas = dekripsiDenganMenggunakanHurufSandiYangDipetakan(pesan, pemetaanHuruf)
    pyperclip.copy(pesanYangTeretas)
    print(pesanYangTeretas)

def menentukanPemetaanRuangKosongHurufSandi():
    #mengembalikan nilai dictionary dalam bentuk huruf-huruf asli yang dipetakan
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}




def tambahkanHurufpadaPemetaan(pemetaanHuruf, katasandi, sampel):
    #pada letterMapping parameternya adalah pesan asli dimana nilai yang dikembalikan oleh fungsi ini dimulai dengan menyalinnya
    #pada cipherword parameternya adalalah nilai string pada ciphertext word
    #parameter candidate memungkinkan kata dalam bahasa inggris pada cipherword dapat di dekrip juga

    #fungsi ini menambahkan kata pada candidate sebagai dekripsi potensial pada cipherletters dalam pemetaan sandi huruf
    pemetaanHuruf = copy.deepcopy(pemetaanHuruf)
    for i in range(len(katasandi)):
        if sampel[i] not in pemetaanHuruf[katasandi[i]]:
            pemetaanHuruf[katasandi[i]].append(sampel[i])
    return pemetaanHuruf


def memotongPemetaan(petaA, petaB):
    #untuk menggabungkan dua peta, buatlah peta kosong, lalu tambahkan huruf yang memungkinkan untuk didekripsi jika ada maka lakukan pada kedua peta
    PemetaanYangDipotong = menentukanPemetaanRuangKosongHurufSandi()
    for huruf in HURUF:

        #daftar kosong berarti "setiap huruf memungkinkan". Pada hal ini hanya salin map lainnya pada masukan
        if petaA[huruf] == []:
            PemetaanYangDipotong[huruf] = copy.deepcopy(petaB[huruf])
        elif petaB[huruf] == []:
            PemetaanYangDipotong[huruf] = copy.deepcopy(petaA[huruf])
        else:
            #jika huruf dalam mapA[letter] ada di dalam mapB[letter] tambahkan huruf pada pemotongan pemetaan[huruf]
            for hurufYangDipetakan in petaA[huruf]:
                if hurufYangDipetakan in petaB[huruf]:
                    PemetaanYangDipotong[huruf].append(hurufYangDipetakan)

    return PemetaanYangDipotong


def mengubahHurufyangsudahselesaiDipetakan(pemetaanHuruf):
    #huruf asli dalam pemetaan dalam map hanya untuk per satu huruf saja yang didekrip dan dapat di ubah dalam bentuk huruf lainnya
    #sebagai contoh, jika 'A' dipetakan pada huruf yang potensial ['M','N'], dan 'B' dipetakan pada ['N'], lalu anda tahu bahwa 'B' harus dipetakan pada 'N',
    #lalu anda dapat mengubah 'N' dari daftar bahwa 'A' dapat dipetakan juga. Maka 'A' dipetakan pada ['M'].
    #sekarang peta 'A' hanya memiliki satu huruf, anda dapat mengubah nya ke 'M' dari daftar kata untuk setiap huruf. (hal inilah mengapa ada perulangan dan pemakaian kembali map
    pemetaanHuruf = copy.deepcopy(pemetaanHuruf)
    ulangiLagi = True
    while ulangiLagi:
        #asumsikan dahulu bahwa hal ini tidak melakukan perulangan lagi
        ulangiLagi = False

        #huruf yang sudah diubah hanya akan menjadi daftar huruf besar saja dan hanya memmungkinkan satu pemetaan dalam pemetaan huruf 
        hurufYangDipecah = []
        for sandiHuruf in HURUF:
            if len(pemetaanHuruf[sandiHuruf]) == 1:
                hurufYangDipecah.append(pemetaanHuruf[sandiHuruf][0])

    #jika satu huruf telah selesai, lalu hal ini tidak berarti dapat menjadi huruf potensial untuk melakukan dekripsi pada chipertext yang berbeda
    #jadi anda harus mengubah hal ini dari daftar yang lainnya
    for sandiHuruf in HURUF:
            for s in hurufYangDipecah:
                if len(pemetaanHuruf[sandiHuruf]) != 1 and s in pemetaanHuruf[sandiHuruf]:
                    pemetaanHuruf[sandiHuruf].remove(s)
                    if len(pemetaanHuruf[sandiHuruf]) == 1:
                        #jika sudah ada huruf yang selesai diproses maka,
                        #diulangi untuk huruf selanjutnya dan seterusnya
                        loopAgain = True
    return pemetaanHuruf


def retasSubSederhana(pesan):
    PetaYangDipotong = menentukanPemetaanRuangKosongHurufSandi()
    daftarKataSandi = bukanHurufatauPolaSpasi.sub('', pesan.upper()).split()
    for kataSandi in daftarKataSandi:
        #membuat pemetaan cipherletter yang baru untuk setiap kata sandi teks
        petaBaru = menentukanPemetaanRuangKosongHurufSandi()

        #polaKata dan polaKata1 adalah dua hal berbeda
        polaKata1 = membuatrumuskata.membuatPolaKata(kataSandi)
        if polaKata1 not in polaKata.seluruhPola:
            continue #jika hal yang dicari tidak ada dalam kamus 

         #tambahkan huruf untuk setiap pemetaan candidate
        for sampel in polaKata.seluruhPola[polaKata1]:
            petaBaru = tambahkanHurufpadaPemetaan(petaBaru, kataSandi, sampel)

        #peta yang dipotong adalah peta yang telah dipotong yang sebelumnya telah ada
        PetaYangDipotong = memotongPemetaan(PetaYangDipotong, petaBaru)

    #pindahkan setiap huruf yang sudah selesai ke dalam daftar lainnya
    return mengubahHurufyangsudahselesaiDipetakan(PetaYangDipotong)


def dekripsiDenganMenggunakanHurufSandiYangDipetakan(sanditeks, pemetaanHuruf):
    #mengembalikan nilai string pada ciphertext yang sudah didekrip dengan pemetaan huruf
    #setiap huruf hasil dekrip yang ambigu akan ditempatkan kembali dengan sebuah "_" underscore


    #buatlah dahulu sebuah kunci sub sederhana dari letterMapping dengan pemetaan
    kunci = ['x'] * len(HURUF)
    for sandiHuruf in HURUF:
        if len(pemetaanHuruf[sandiHuruf]) == 1:
            #jika hanya ada satu huruf saja, lalu tambahkan hal ini ke dalam kunci
            indeksKunci = HURUF.find(pemetaanHuruf[sandiHuruf][0])
            kunci[indeksKunci] = sandiHuruf
        else:
            sanditeks = sanditeks.replace(sandiHuruf.lower(), '_')
            sanditeks = sanditeks.replace(sandiHuruf.upper(), '_')
    kunci = ''.join(kunci)

    #dengan kunci yang telah anda buat, lakukan dekripsi pesan asli
    #pesanDekripsi harus sesuai dengan subsandisederhana
    return subsandisederhana.pesanDekripsi(kunci, sanditeks)


if __name__ == '__main__':
    main()
#program ini bekerja hanya jika spasi tidak di enkripsi
#memiliki 403,291,461,126,605,635,584,000,000 kemungkinan
#kemungkinan melakukan bruteforce hampir beberapa ratus tahun dan hampir tidak terpecahkan
#hal ini disebut dengan "polyalphabetic" oleh sandi Vigenère
#saat program sudah berjalan akan membutuhkan beberapa waktu untuk komputer berjalan normal
#komputer anda baik-baik saja dan begitupun dengan program ini
#hanya saja membutuhkan waktu untuk tidak sekedar mengkompilasi
#namun juga menghasilkan program baru bernama polaKata.py
#data polaKata.py berasal dari dictionary.txt

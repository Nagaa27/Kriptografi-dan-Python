################################################################
# Analisis Frekuensi                                                                                         #
# Editor : Matius Celcius Sinaga                                                                        #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

#dasar frekuensi diambil dari Wikipedia http://en.wikipedia.org/wiki/Letter_frequency
frekuensiPenggunaanHuruf = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#pada fungsi ini akan mengambil parameter string dan menghasilkan dictionary/kamus
#dimana hal ini dapat menghitung seberapa sering setiap huruf muncul dalam string
def menghitungJumlahHuruf(pesan):
      #menghasilkan sebuah daftar kamus dengan kunci dari setiap huruf dan nilai
    #dimana hal ini dihitung berapa kali hal tersebut muncul dalam sebuah parameter pesan
    hitungHuruf = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for huruf in pesan.upper():
        if huruf in HURUF:
            hitungHuruf[huruf] += 1

    return hitungHuruf


def menentukanNilaipadaDasar(x):
    return x[0]

#pada fungsi ini akan mengambil parameter string dan menghasilkan string dari 26 huruf
#diubah dari yang paling sering muncul menjadi parameter yang paling terakhir muncul
def menentukanJumlahPerintah(pesan):
    #mengembalikan sebuah nilai dengan huruf alpabet yang disusun dengan
    #mengatur frekuensi huruf yang muncul paling sering dalam parameter pesan
    #pertama, tentukan dictionary/kamus untuk setiap kata dan frekuensi yang dihitung
    hurufpadaFrekuensi = menghitungJumlahHuruf(pesan)
    #kedua, buatlah sebuah dictionary/kamus dimana setiap frekuensi yang dihitung
    #pada setiap huruf dengan frekuensinya
    frekuensipadaHuruf = {}
    for huruf in HURUF:
        if hurufpadaFrekuensi[huruf] not in frekuensipadaHuruf:
            frekuensipadaHuruf[hurufpadaFrekuensi[huruf]] = [huruf]
        else:
            frekuensipadaHuruf[hurufpadaFrekuensi[huruf]].append(huruf)

    #ketiga, masukkan setiap daftar dari kata dalam pengembalian "ETAOIN"
    #lalu ubah hal tersebut menjadi kalimat
    for frekuensi in frekuensipadaHuruf:
        frekuensipadaHuruf[frekuensi].sort(kunci=ETAOIN.find, reverse=True)
        frekuensipadaHuruf[frekuensi] = ''.join(frekuensipadaHuruf[frekuensi])

    #keempat, ubah setiap kamus freqToLetter menjadi list pertukaran
    #hubungkan (kunci, nilai), lalu urutkan hal tersebut
    frekuensiBerpasangan = list(frekuensipadaHuruf.items())
    frekuensiBerpasangan.sort(kunci=menentukanJumlahPerintah, reverse=True)

    #kelima, kata yang sudah diubahkan sesuai dengan frekuensi
    #ekstrak seluruh kata dengan kalimat penutup
    penugasanFrekuensi = []
    for frekuensiBerpasangan in frekuensiBerpasangan:
        penugasanFrekuensi.append(frekuensiBerpasangan[1])

    return ''.join(penugasanFrekuensi)

#pada fungsi ini akan mengambil parameter string dan menghasilkan integer/bilangan bulat
#dari 0 hingga 12 dari string yang paling cocok nilainya
def JumlahfrekuensiYangCocok(pesan):
    #menampilkan jumlah kata yang sesuai dengan pesan
    #parameter memiliki frekuensi kata yang dapat dibandingkan dengan
    #kata berfrekuensi dalam bahasa inggris
    #jika cocok jumlah kata 6 terbanyak dan 6 terakhir yang memiliki frekuensi
    penugasanFrekuensi = menentukanPenugasanFrekuensi(pesan)

    jumlahyangCocok = 0
    #cari berapa jumlah yang sesuai dengan kata terbanyak yang ada disana
    for hurufYangUmum in ETAOIN[:6]:
        if hurufYangUmum in penugasanFrekuensi[:6]:
            jumlahyangCocok += 1
    #cari berapa jumlah yang sesuai dengan kata terbanyak yang ada disana
    for hurufYangtidakUmum in ETAOIN[-6:]:
        if hurufYangtidakUmum in freqOrder[-6:]:
            jumlahyangCocok += 1

    return jumlahyangCocok

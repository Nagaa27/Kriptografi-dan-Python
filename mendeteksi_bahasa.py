################################################################
# Deteksi Bahasa                                                                                             #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

#untuk menggunakan program ini gunakan python shell
#ketik "import deteksibahasa" (tanpa tanda kutip)
#program ini harus berada pada satu folder bersama "dictionary.txt"
#"dictionary.txt" file berisi seluruh bahasa silahkan anda ubah
#atau cari dictionary lainnya, Github atau penyedia source code lain
HurufBESAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Huruf_Dan_Spasi = HurufBESAR + HurufBESAR.lower() + ' \t\n'

#melakukan pengenalan untuk memulai jalankanKamus
#pada bagian ini akan melakukan pengecekan dan membuka file dictionary
#apabila cekKata sudah benar maka program akan selesai
def memuatKamus():
    fileKamus = open('dictionary.txt')
    cekKata = {}
    for kata in fileKamus.read().split('\n'):
        cekKata[kata] = None
    fileKamus.close()
    return cekKata

#cek bahasa apakah sama dengan fungsi dengan memuat kamus
KATA_BAHASA = memuatKamus()

#melakukan pengenalan untuk melakukan perhitungan jumlah kata yang digunakan
#jika ditemukan kata yang cocok atau dimungkinkan akan dibandingkan dengan
#jumlah kata yang cocok
def hitungJumlahKata(pesan):
    pesan = pesan.upper()
    pesan = bukanKata(pesan)
    kemungkinanKata = pesan.split()

    if kemungkinanKata == []:
        #jika tidak ditemukan satupun huruf maka hasilkan nilai 0
        return 0.0 
    cocok = 0
    for kata in kemungkinanKata:
        if kata in KATA_BAHASA:
            cocok += 1
    return float(cocok) / len(kemungkinanKata)

#melakukan pendefinisian yang tidak termasuk di dalam kata
def bukanKata(pesan):
    hurufSaja = []
    for symbol in pesan:
        if symbol in Huruf_Dan_Spasi:
            hurufSaja.append(symbol)
    return ''.join(hurufSaja)

#melakukan pendefinisian dari cekBahasa yang dimana terdapat pesan
#jumlah kata dan huruf yang diijinkan dalam program yang akan dimuat
#secara umum, 20% dari kata seharusnya ada pada file dictionary
#dan 85% dari seluruh karakter di dalam pesan berisi kata dan spasi
#bukan tanda baca atau angka
def cekBahasa(pesan, IjinkanJumlahKata=20, IjinkanJumlahHuruf=85):
    kataYangCocok = hitungJumlahKata(pesan) * 100 >= IjinkanJumlahKata
    nomorHuruf = len(bukanKata(pesan))
    IjinkanJumlahKalimat = float(nomorHuruf) / len(pesan) * 100
    hurufYangCocok = IjinkanJumlahKalimat >= IjinkanJumlahHuruf
    return kataYangCocok and hurufYangCocok


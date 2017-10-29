#############################################################
# Meretas Sandi Kamus Vigenere                                                                    #
# Editor : Matius Celcius Sinaga                                                                      #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                 #
#############################################################

#itertools dan re sudah tersedia saat anda melakukan instalasi python
import itertools, re
import sandivigenere, pyperclip, analisisfrekuensi, deteksibahasa

HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#jika True maka program tidak akan mencoba menampilkan pesan
MODE_SENYAP = False 

FREKUENSI_HURUF_TERBESAR = 4 
PANJANG_KUNCI_MAKSIMAL = 16 
POLA_YANG_BUKAN_HURUF = re.compile('[^A-Z]')


def main():
    sanditeks = """Mltv Gsfhbaif Fukqhy ial i Vjutbab emtamgsfivquf, xozqwamn, vzshfagifqet, tvx uamicnwd svqyffilb. Bw ial pcytlr qhxxuxvnaml bv nzq dxdydapfmhl af vwghgtxz muuegky, hdooqxazg t nijyaeqmsfihv ix fhx kifoeibm gr "aeoijutau" ufp "chujmfamqif" iimp nzq Tnzcfs mtkbaze. Mclazg ba qapeeg wgzsblyjqd mw vw fhx nultek wz uamicnwd svqyfoe tvx sdtbncuuae qhlqleqawzcx. Lojunz Eijxd Pil AU, Tnzcfs whzewp fhz nzq Ghdyjzmxvn Uadx ihv Oyipyj Ecawid (SCVA) ul Nlxbwzxer Xujw, Bkqnsun'l kivqbkmucunz kyffrx. Nij m tbuy zq wta bwmd hn Bmf 8, tam mwotbwh jqsiwhkubem zgd Gxzgsz ntdud orrxnszaegmae. Hx lynusxl u fgmuml gr txkbfuqnmm xar uzyswigo Awdmtv wabhxzm, azcecxazg mpy eqtawx gr tam vgybx, ih wxevblgyevpufuctt gsohbvy ltam kimxd yqhv eembcfss ywl lte Xvcyya fiwzunx. Izlqr mpy omr am qgdkxl ul fhx Vuluogif Htylqwsx Ltjijmthzs, otekm bw orxinwp ogm ix fhx ncjet wmmasnl nij m smwlwp-pkwajmm vwghgtxz, nzq AVM. Cf 1948 Fukqhy vobvyv Yaq Vyoyag'a Wgypnbcfs Ltjijmthzs sf Mtvwzqsmml Mziomlkutr, ebwde am ukeilbyv un mpy vqvxtihyegb ix fhx Uufohxanwd chujmfeka ufp bxkueq igbyjqsmmx az mtbbwyamqwsx bbwfgsy. Am qjatx i jsbek wh lte vpyeuctt vseil wz earipiyqnxack, mnw xlwpivbyv asvqfdmtbva utefqwsx rxiwluoga mmoh ta nzq Bxtimeoo-Hbsnomqhkwy kmuufihv, qzuca eyjq fbzml ablmlnqd bv nzq 1960s. Mclazg'l pieasxfosximg lweuebyv un t klayigif hdolmwmfihv cf 1952, ihxv bgyolmrmml tknk iekm mlule qfdqgtt cf fhx Chafew Scfsdhu. Bw mcvmjlqd mzysfmxvn outa nyemlx pijyogmm (utefqwsx ctanjmtbwh) se ag iflqrginahe mw jjushv. Nmdigo xaqd bv 1954, dmet hdyj fwh eywws umzgde aqm 42fp bbznzpar, nlgy crihape iwckanbva. Sz igyowet wmnwdmbvyv fhtb bae dxinz ial aoaoiwm; bae mhbbwd agl mgye hbbwds umfaqvxl bae dxinz ial iwuudxvnsx. Og 10 Ayhfefjyj 2009, roetiounz ih Aztxzhwf ctujsugg, Jlafilp Jjumx Ucfusmml Yarwwh Tdopv gspe tv ixrivqud buutcu mphtiyk og jyzmly wz lte Uzclusa oinqrguyff fhz "nzq aixudxigo qsk hx euk frxinwp." Al wz Emy 2012 t xlahamm gwybxz'm tule euk neywlw fhx Pimee hn Fgddl ebaoh pwodp gkihl Fukqhy m sminmfokg jsddhv cx qntknwp."""
    pesanYangTeretas = meretasVigenere(sanditeks)

    if pesanYangTeretas != None:
        print('menyalin pesan yang sudah teretas ke dalam layar:')
        print(pesanYangTeretas)
        pyperclip.copy(pesanYangTeretas)
    else:
        print('Gagal melakukan peretasan terhadap enkripsi.')


def cariRuangKosongberangkaiBerulang(pesan):
    #akan mencoba pesan dan menetapkan 3 hingga 5 huruf untuk dirangkai dan diulang
    #menghasilkan  kunci dari rangkaian dan nilai pada daftar kosong antara jumlah huruf yang diulang
   
    #gunakan jenis huruf yang umum untuk mengubah pesan dan non pesan dari pesan
    pesan = POLA_YANG_BUKAN_HURUF.sub('', pesan.upper())

    #mengkompilasi daftar panjang rangkaian huruf yang ditemukan dalam pesan    rangkaianRuangKosong = {}
     for panjangRangkaian in range(3, 6):
        for memulaiRangkaian in range(len(pesan) - panjangRangkaian):
            #mendeminasikan bagaimana rangkaian dan menyimpanya 
            rangkaian = pesan[memulaiRangkaian:memulaiRangkaian + panjangRangkaian]

            #mencari rangkaian dalam pesan
            for i in range(memulaiRangkaian + panjangRangkaian, len(pesan) - panjangRangkaian):
                if pesan[i:i + panjangRangkaian] == rangkaian:
                    #menemukan perulangan pada rangkaian
                    if rangkaian not in rangkaianRuangKosong:
                        rangkaianRuangKosong[rangkaian] = [] # initialize blank list

                    #menambahkan ruang kosong sebagai penghubung diantara perulangan
                    #rangkaian dan rangkaian asli
                    rangkaianRuangKosong[rangkaian].append(i - memulaiRangkaian)
    return rangkaianRuangKosong


def menentukanfaktorYangberguna(angka):
    #menghasilkan daftar factor yang berguna dan menggunakannya
    #tidak kurang dari MAX_KEY_LENGTH + 1. Sebagai contohnya adalah (144)
    # menghasilkan [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]

    #angka yang kurang dari 22 tidak memiliki faktor
    if angka < 2:
        return [] 

    #daftar factor yang telah ditemukan
    faktor = [] 

    #ketika menemukan factor, anda hanya harus mencek nilai bilangan bulat yang mencapai
MAX_KEY_LENGTH.
    for i in range(2, PANJANG_KUNCI_MAKSIMAL + 1): 
        if angka % i == 0:
            faktor.append(i)
            faktor.append(int(angka / i))
    if 1 in faktor:
        faktor.remove(1)
    return list(set(faktor))


def menetapkanSatudasarIndex(x):
    return x[1]


def menentukanFaktorYangPalingUmum(faktorRangkaian):
    #hitung berapa banyak perulangan yang ditetapkan sebagai factor yang ditemukan pada rangkaian faktor
    menghitungFaktor = {} # key is a factor, value is how often if occurs

    #rangkaian factor adalah bentuk-bentuk rangkaian yang memiliki daftar nilai ruang kosong 
    #pada rangkaian  factor memiliki nilai seperti: {'GFD': [2, 3, 4, 6, 9, 12,
    # 18, 23, 36, 46, 69, 92, 138, 207], 
    for rangkaian in faktorRangkaian:
        daftarFaktor = faktorRangkaian[rangkaian]
        for faktor in daftarFaktor:
            if faktor not in menghitungFaktor:
                menghitungFaktor[faktor] = 0
            menghitungFaktor[faktor] += 1

    #setelah itu masukkan factor dan hitung lalu buat daftarnya
    menghitungdenganFaktor = []
    for faktor in menghitungFaktor:
        #tidak termasuk factor yang lebih besar dari  MAX_KEY_LENGTH
        if faktor <= PANJANG_KUNCI_MAKSIMAL:
            #faktor yang dihitung adalah daftar dari factor dan hitung faktor
            #faktor yang dihitung memiliki nilai seperti [(3, 497), (2, 487), ...]
            menghitungdenganFaktor.append( (faktor, menghitungFaktor[faktor]) )

    #urutkan daftar dengan factor yang dihitung
    menghitungdenganFaktor.sort(key=menetapkanSatudasarIndex, reverse=True)

    return menghitungdenganFaktor

def pengujianKasiski(sanditeks):
    #menetapkan rangkaian dari 3 hingga 5 huruf yang didapatkan dari perulangan yang berkali-kali di dalam pesan teks,
    #perulangan jarak rangkaian memiliki nilai seperti
    # {'EXG': [192], 'NAF': [339, 972, 633], ... }
    melakukanUrutanRuangkosong = cariRuangKosongberangkaiBerulang(sanditeks)

    #menentukan penetapan factor yang paling umum sebagai dekripsi dari factor rangkaian
    faktorRangkaian = {}
    for rangkaian in melakukanUrutanRuangkosong:
        faktorRangkaian[rangkaian] = []
        for jarak in melakukanUrutanRuangkosong[rangkaian]:
            faktorRangkaian[rangkaian].extend(menentukanfaktorYangberguna(jarak))

    #menentukan penetapan factor yang paling umum sebagai dekripsi dari factor yang dihitung
    menghitungdenganFaktor = menentukanFaktorYangPalingUmum(faktorRangkaian)

    #ekstrak factor yang dihitung dari factor yang dihitung dan masukkan seluruhnya dalam panjang kunci 
     #yang menyerupai atau sama dengan begitu akan lebih mudah untuk digunakan nantinya 
    seluruhKunciyangMemungkinkan = []
    for duaBilangan in menghitungdenganFaktor:
        seluruhKunciyangMemungkinkan.append(duaBilangan[0])

    return seluruhKunciyangMemungkinkan


def menentukanNSubKunciHuruf(n, panjangKunci, pesan):
    #menghasilkan setiap nilai ke-N pada setiap panjang kunci yang ditentukan oleh huruf dalam teks
    #contoh menetapkan nilai ke –N sub kunci huruf (1, 3, 'ABCABCABC') menghasilkan 'AAA'
    #      menetapkan nilai ke –N sub kunci huruf (2, 3, 'ABCABCABC') menghasilkan 'BBB'
    #      menetapkan nilai ke –N sub kunci huruf (3, 3, 'ABCABCABC') menghasilkan 'CCC'
    #      menetapkan nilai ke –N sub kunci huruf (1, 5, 'ABCDEFGHI') menghasilkan 'AF'

    #menggunakan ekspressi yang umum untuk menentukan jenis huruf dan bukan huruf pada pesan
    pesan = POLA_YANG_BUKAN_HURUF.sub('', pesan)

    i = n - 1
    huruf = []
    while i < len(pesan):
        huruf.append(pesan[i])
        i += panjangKunci
    return ''.join(huruf)


def mencobaMeretasDenganPanjangKunci(sanditeks, kunciYangpalingmemungkinkan):
    #menetapkan huruf yang paling sering ada disetiap huruf dalam kunci
    sanditeksKapital = sanditeks.upper()
    #seluruh nilai frekuensi yang ada pada panjang huruf yang menyerupai dalam panjang kunci yang paling cocok jumlahnya pada daftar
    #dalam dafatr terdapat daftar frekuensi nilai 
    seluruhNilaiFrekuensi = []
    for nilaiKeN in range(1, kunciYangpalingmemungkinkan + 1):
        hurufKeN = menentukanNSubKunciHuruf(nilaiKeN, kunciYangpalingmemungkinkan, sanditeksKapital)

        #nilai frekuensi adalah daftar dari penyatuan dua hal seperti huruf, bahasa, frekuensi dan nilai yang cocok
        # daftar yang telah diurutkan dengan kesamaan nilai contohnya dari yang paling banyak kesamaan
        #silahkan cek dari nilai frekuensi kecocokan bahasa pada program analisis frekuensi
        frekuensiNilai = []
        for kunciYangMemungkinkan in HURUF:
            teksTerdekripsi = sandivigenere.dekripsiPesan(kunciYangMemungkinkan, hurufKeN)
            kunciDanFrekuensiYangcocok = (kunciYangMemungkinkan, analisisfrekuensi.JumlahfrekuensiYangCocok(teksTerdekripsi))
            frekuensiNilai.append(kunciDanFrekuensiYangcocok)
        #urutkan dengan kecocokan nilai
        frekuensiNilai.sort(key=menetapkanSatudasarIndex, reverse=True)

        seluruhNilaiFrekuensi.append(frekuensiNilai[:FREKUENSI_HURUF_TERBESAR])

    if not MODE_SENYAP:
        for i in range(len(seluruhNilaiFrekuensi)):
            #gunakan i+1 untuk huruf yang pertama disebut dengan  huruf ke 0
            print('Kemungkinan huruf yang cocok  %s dengan kunci: ' % (i + 1), end='')  
            for frekuensiNilai in seluruhNilaiFrekuensi[i]:
                print('%s ' % frekuensiNilai[0], end='')
	#menampilkan baris baru
            print() 

    #coba dengan setiap kombinasi dari yang paling cocok dengan huruf pada setiap posisi pada kunci
    for terindeks in itertools.product(range(FREKUENSI_HURUF_TERBESAR), repeat=kunciYangpalingmemungkinkan):
        #membuat kunci yang memungkinkan dari huruf dalam nilai  frekuensi keseluruhan
        kunciYangMemungkinkan = ''
        for i in range(kunciYangpalingmemungkinkan):
            kunciYangMemungkinkan += seluruhNilaiFrekuensi[i][terindeks[i]][0]

        if not MODE_SENYAP:
            print('Mencoba dengan kunci: %s' % (kunciYangMemungkinkan))

        pesanTerdekripsi = sandivigenere.dekripsiPesan(kunciYangMemungkinkan, sanditeksKapital)

        if deteksibahasa.cekBahasa(pesanTerdekripsi):
            #menentukan teks awal yang dapat diretas menjadi bentuk asli
            bentukAsli = []
            for i in range(len(sanditeks)):
                if sanditeks[i].isupper():
                    bentukAsli.append(pesanTerdekripsi[i].upper())
                else:
                    bentukAsli.append(pesanTerdekripsi[i].lower())
            pesanTerdekripsi = ''.join(bentukAsli)

            #cek dengan pengguna apabila kunci telah ditemukan
            print('Possible encryption hack with key %s:' % (kunciYangMemungkinkan))
	#hanya menampilkan 200 karakter
            print(pesanTerdekripsi[:200]) 
            print()
            print('Untuk berhenti tekan D, untuk melanjutkan tekan Enter:')
            respon = input('> ')

            if respon.strip().upper().startswith('D'):
                return pesanTerdekripsi

    #tidak menemukan bahasa dengan dekripsi yang ditentukan dan menghasilkan nilai kembali 0 (none)
    return None


def meretasVigenere(sanditeks):
    #lakukan pengujian Kasiski untuk menggambarkan bagaimana panjang sandi teks enkripsi dari kunci
    seluruhKunciyangMemungkinkan = pengujianKasiski(sanditeks)
    if not MODE_SENYAP:
        panjangKunciString = ''
        for panjangKunci in seluruhKunciyangMemungkinkan:
            panjangKunciString += '%s ' % (panjangKunci)
        print('Pengujian Kasiski menghasilkan apa yang disebut dengan panjang kunci yang menyerupai tersebut : ' + panjangKunciString + '\n')

    for panjangKunci in seluruhKunciyangMemungkinkan:
        if not MODE_SENYAP:
            print('Mencoba meretas dengan panjang kunci %s (%s kemungkinan kunci)...' % (panjangKunci, FREKUENSI_HURUF_TERBESAR ** panjangKunci))
        pesanYangTeretas = mencobaMeretasDenganPanjangKunci(sanditeks, panjangKunci)
        if pesanYangTeretas != None:
            break

    #jika tidak ditemukan panjang kunci dengan pengujian Kasiski maka lakukan brute-force pada panjang kunci
    if pesanYangTeretas == None:
        if not MODE_SENYAP:
            print('Tidak dapat meretas pesan dengan panjang kunci. Panjang kunci brute-force...')
        for panjangKunci in range(1, PANJANG_KUNCI_MAKSIMAL + 1):
            #tidak memerlukan pengecekan kembali pada pengujian Kasiski
            if panjangKunci not in seluruhKunciyangMemungkinkan:
                if not MODE_SENYAP:
                    print('Mencoba meretas dengan panjang kunci %s (%s kunci yang memungkinkan)...' % (panjangKunci, FREKUENSI_HURUF_TERBESAR ** panjangKunci))
                pesanYangTeretas = mencobaMeretasDenganPanjangKunci(sanditeks, panjangKunci)
                if pesanYangTeretas != None:
                    break
    return pesanYangTeretas


#jika program sudah berjalan dengan semestinya dan seluruh program yang diimport berjalan dengan lancar
if __name__ == '__main__':
    main()

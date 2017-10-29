################################################################
# Meretas Sandi Transposisi                                                                              #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

#jalankan program terlebih dahulu tekan enter pada shell saat melakukan proses
import pyperclip, deteksibahasa, dekripsitransposisi

def main():
    #anda akan melakukan bruteforce pada pesan ini
    #silahkan dicopy-paste jika ingin melakukan eliminasi
    pesanSaya = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
    #pada pesanSaya memiliki 3 tanda kutip diakhir dan diawal
    #hal tersebut digunakan untuk menandakan bahwa pesanSaya
    #baris-baris yang berbeda

    #proses menampilkan apakah berhasil atau gagal dalam melakukan peretasan
    pesanSaya = retasTransposisi(pesanSaya)

    #jika anda gagal
    if pesanYangTeretas == None:
        print('Gagal melakukan peretasan pada enkripsi.')
    else:
        print('Menyalin pesan yang teretas ke dalam layar:')
        print(pesanYangTeretas)
        #pyperclip harus berada satu folder dengan program
        pyperclip.copy(pesanYangTeretas)

def retasTransposisi(pesan):
    print('Sedang meretas...')

    #saat program python dalam kondisi berjalan
    #anda bisa melakukan pemberhentian setiap kali
    #anda menekan Ctrl-C pada Windows
    #atau Ctrl-D pada Mac dan Linux
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    #disini program melakukan bruteforce
    #dengan mengulangi setiap kunci yang memungkinkan
    for kunci in range(1, len(pesan)):
        print('Mencoba kunci #%s...' % (kunci))

        #decryptMessage berasal dari program dekripsitransposisi
        pesanTerdekripsi = dekripsitransposisi.dekripsiPesan(kunci, pesan)

        if deteksibahasa.cekBahasa(pesanTerdekripsi):
            #apabila kunci telah ditemukan
            print()
            print('Kemungkinan dapat di retas:')
            print('Kunci %s: %s' % (kunci, pesanTerdekripsi[:100]))
            print()
            print('Tekan D untuk berhenti dan Enter untuk melanjutkan peretasan:')
            respon = input('> ')

            if respon.strip().upper().startswith('D'):
                return pesanTerdekripsi

    return None

if __name__ == '__main__':
    main()

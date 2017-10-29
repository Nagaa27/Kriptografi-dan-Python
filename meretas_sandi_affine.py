################################################################
# Meretas Sandi Affine                                                                                     #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                        #
################################################################

import pyperclip, sandiaffine, deteksibahasa, kriptomath

MODE_SENYAP = False

def main():
    pesanSaya = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG'<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""

    pesanYangTeretas = retasAffine(pesanSaya)

    if pesanYangTeretas != None:
        #seluruh teks awal yang telah ditampilkan akan di salin ke dalam layar
        print('Sedang menyalin pesan yang sudah diretas:')
        print(pesanYangTeretas)
        pyperclip.copy(pesanYangTeretas)
    else:
        print('Gagal melakukan peretasan terhadap enkripsi.')


def retasAffine(pesan):
    print('Sedang mencoba meretas...')

    print('(Tekan Ctrl-C atau Ctrl-D untuk berhenti setiap kali.)')

    #mencoba brute-force dengan seluruh perulangan dan mencoba kunci yang memungkinkan     for kunci in range(len(sandiaffine.SYMBOLS) ** 2):
        kunciA = sandiaffine.cariBagianKunci(kunci)[0]
        if kriptomath.gcd(kunciA, len(sandiaffine.SYMBOLS)) != 1:
            continue

        pesanTerdekripsi = sandiaffine.dekripsiPesan(kunci, pesan)
        if not MODE_SENYAP:
            print('Mencoba dengan kunci %s... (%s)' % (kunci, pesanTerdekripsi[:40]))

        if deteksibahasa.cekBahasa(pesanTerdekripsi):
            #apabila pengguna(user) melakukan pengecekan
            #terhadap kunci terdekripsi yang telah ditemukan
            print()
            print('Enkripsi dapat diretas:')
            print('Kunci: %s' % (kunci))
            print('Pesan Terdekripsi: ' + pesanTerdekripsi[:200])
            print()
            print('Tekan D untuk selesai, atau tekan Enter untuk melanjutkan peretasan:')
            respon = input('> ')

            if respon.strip().upper().startswith('D'):
                return pesanTerdekripsi
    return None


#jika program berjalan dengan sesuai juga dengan modul yang diimnport
#fungsi main dimulai dari sini
if __name__ == '__main__':
    main()

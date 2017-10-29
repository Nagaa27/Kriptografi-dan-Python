################################################################
# Membuat Pola Kata                                                                                       #
# Editor : Matius Celcius Sinaga                                                                         #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

#modul pprint memiliki fungsi dalam pretty printing nilai
#dimana hal ini berguna untuk menampilkan kamus dan daftar nilai pada layar
#pprint sudah tersedia saat anda melakukan instalasi Python
#anda hanya perlu memanggil/import saja
import pprint

def membuatPolaKata(kata):
    #menghasilkan sebuah string dari pola yang diberikan oleh kata
    #contohnya adalah '0.1.2.3.4.1.2.3.5.6' dan selanjutnya
    kata = kata.upper()
    angkaSelanjutnya = 0
    nomorHuruf = {}
    polaKata = []

    for huruf in kata:
        if huruf not in nomorHuruf:
            nomorHuruf[huruf] = str(angkaSelanjutnya)
            angkaSelanjutnya += 1
        polaKata.append(nomorHuruf[huruf])
    return '.'.join(polaKata)

def main():
    seluruhPola = {}

    fo = open('dictionary.txt')
    daftarKata = fo.read().split('/n')
    fo.close()

    for kata in daftarKata:
        #tentukan pola untuk setiap string didalam daftarKata
        pola = membuatPolaKata(kata)

        if pola not in seluruhPola:
            seluruhPola[pola] = [kata]
        else:
            seluruhPola[pola].append(kata)

    #kode program ini akan menghasilkan kode program polaKata.py
    #dan program polaKata.py sangat besar dan memiliki statement yang luas
    fo = open('polaKata.py', 'w')
    fo.write('seluruhPola = ')
    fo.write(pprint.pformat(seluruhPola))
    fo.close()

if __name__ == '__main__':
    main()

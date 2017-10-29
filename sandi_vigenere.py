################################################################
# Vigenère Cipher ( Sandi Subtitusi Polyalphabetic )                                         #
# Editor : Matius Celcius Sinaga                                                                        #
# Author : # http://inventwithpython.com/hacking (BSD Licensed)                         #
################################################################

import pyperclip

HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#pada fungsi main terdapat variabel pesan, kunci dan mode sebelum program dijalankan
#pada mode anda dapat menetapkan apakah program akan melakukan enkripsi atau dekripsi
def main():
    pesanSaya = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted."""
    kunciSaya = 'MATIUS'
    #silahkan ubah untuk melakukan enkripsi atau dekripsi disini
    modeSaya = 'enkripsi' 

    if modeSaya == 'enkripsi':
        ubah = enkripsiPesan(kunciSaya, pesanSaya)
    elif modeSaya == 'dekripsi':
        ubah = dekripsiPesan(kunciSaya, pesanSaya)

    print('%sed pesan : ' % (modeSaya.title()))
    print(ubah)
    pyperclip.copy(ubah)
    print()
    print('Pesan akan disalin kedalam papan klip.')

#pada bagian ini menjelaskan bagaimana enkripsi berjalan
def enkripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'enkripsi')

#pada bagian ini menjelaskan bagaimana dekripsi berjalan
def dekripsiPesan(kunci, pesan):
    return ubahPesan(kunci, pesan, 'dekripsi')

def ubahPesan(kunci, pesan, mode):
    ubah = [] 
#menyimpan pesan enkripsi dan dekripsi

    kunciIndex = 0
    kunci = kunci.upper()

    for symbol in pesan: 
    #akan dilakukan pada seluruh karakter dalam pesan
        nomor = HURUF.find(symbol.upper())
        if nomor != -1: #-1 berarti symbol.upper() tidak ditemukan didalam HURUF
            if mode == 'enkripsi':
                nomor += HURUF.find(kunci[kunciIndex]) #tambahkan jika dienkripsi
            elif mode == 'dekripsi':
                nomor -= HURUF.find(kunci[kunciIndex]) #kurangi jika melakukan dekripsi

            nomor %= len(HURUF) 
           
            #tambahkan pada hasil symbol enkrip/dekrip yang sudah diubahkan
            if symbol.isupper():
                ubah.append(HURUF[nomor])
            elif symbol.islower():
                ubah.append(HURUF[nomor].lower())

            kunciIndex += 1 
            #ubah kunci yang akan dipakai selanjutnya
            if kunciIndex == len(kunci):
                kunciIndex = 0

        else:
            #symbol tidak berada pada HURUF, maka tambahkan hal tersebut dan ubahkan
            ubah.append(symbol)

    return ''.join(ubah)

#jika sandiVigenere.py sudah berjalan termasuk seluruh modulnya
#panggil fungsi main
if __name__ == '__main__':
    main()

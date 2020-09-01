# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower
alay = "aKu KeCe AbieeeZZZzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + ' is lower = ' + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya boolean
print(salam + ' is upper = ' + str(apakah_upper))

batas = "PR".center(20,'+')
print(batas)
# isalpha() <-- untuk mengecek semuanya huruf
huruf = 'abcde'.isalpha()
print(str(huruf))
# isalnum() <-- huruf dan angka
hurufdananka = 'abcde1'.isalnum()
print(str(hurufdananka))
# isdecimal() <-- angkasaja
angka = '123567'.isdecimal()
print(str(angka))
# isspace() <-- spase, tab, newline \n
spase = ' \t\n'.isspace()
print(str(spase))
print(batas)

# istitle() <-- semua kata dimulai dengan huruf besar
judul = 'It Is Okey Not To Be Orkay'
cek_judul = judul.istitle() # hasilnya boolean
print(judul + 'is title = ' + str(cek_judul))

## ngecek komponen startswith() endswith() <-- Keren
cek_start = 'Sangjangnim Oppa'.startswith('Sangjangnim')
print("start = " + str(cek_start))

cek_end = 'Sangjangnim Oppak'.endswith('Oppak')
print('End = ' + str(cek_end))

## Penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust(), center()

kanan = 'kanan'.rjust(10)
print("'"+kanan+"'")

kiri = 'kiri'.ljust(10)
print("'"+kiri+"'")

tengah = 'tengah'.center(20,'-')
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = 'tengah'.strip('-') # menghilangkan tanda -
print("'"+tengah+"'")